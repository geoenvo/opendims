import sys
from datetime import datetime, timedelta

from django.conf import settings

import tweepy
from tweepy import OAuthHandler

from reports.models import Report, Event, Source as Report_Source
from .models import Source


def report_scheduled_job():
    consumer_key = settings.CONSUMER_KEY
    consumer_secret = settings.CONSUMER_SECRET
    access_token = settings.ACCESS_TOKEN
    access_secret = settings.ACCESS_SECRET

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    max_tweets = 100
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    sources = Source.objects.filter(status='ACTIVE')

    for active_source in sources:
        keywords = active_source.keywords.all()
        for a_keyword in keywords:
            query = a_keyword.keyword
            searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
            for status in searched_tweets:
                tweet_localcreatedtime = status.created_at + timedelta(hours=7)
                diff = datetime.now() - tweet_localcreatedtime
                diff_hours = diff.total_seconds()/3600
                if diff_hours <= 1:
                    new_event_create = Event(
                        disaster=active_source.disaster
                    )
                    new_event_create.save()
                    note = status.text.translate(non_bmp_map)
                    new_report_create = Report(
                        note=note,
                        event=new_event_create,
                        source=Report_Source.objects.get(code='TWT')
                    )
                    new_report_create.save()
