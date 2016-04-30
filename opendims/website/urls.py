from __future__ import unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^post/category/(?P<category_slug>[-\w]+)/$',
        views.PostListView.as_view(),
        name='post_list'
    ),
    url(
        r'^post/(?P<pk>\d+)/(?P<slug>[-\w]+)/$',
        views.PostDetailView.as_view(),
        name='post_detail'
    )
]
