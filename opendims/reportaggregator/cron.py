import sys
from datetime import datetime, timedelta

from django.conf import settings
from django.utils.encoding import smart_str

import tweepy
from tweepy import OAuthHandler

from reports.models import Report, Source as Reports_Source
from .models import Source


def report_scheduled_job():
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    access_token = settings.ACCESS_TOKEN
    access_secret = settings.ACCESS_SECRET
    max_tweets = settings.MAX_TWEETS

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)

    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    sources = Source.objects.filter(status='ACTIVE', type='TWITTER')

    for active_source in sources:
        keywords = active_source.keywords.all()
        for a_keyword in keywords:
            query = a_keyword.keyword
            searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
            source = Reports_Source.objects.get(code='TWT')
            for status in searched_tweets:
                tweet_localcreatedtime = status.created_at + timedelta(hours=7)
                diff = datetime.now() - tweet_localcreatedtime
                diff_hours = diff.total_seconds() / 3600
                if diff_hours <= 1:
                    note = status.text.translate(non_bmp_map)
                    note = "[{}] {}".format(active_source.disaster, smart_str(note))
                    new_report = Report(
                        note=note,
                        source=source
                    )
                    new_report.save()
