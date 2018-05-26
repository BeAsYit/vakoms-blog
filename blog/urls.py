from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^post/(?P<pk>\d+)/comment_reply/$', views.reply_to_comment, name='reply_to_comment'),
    url(r'^posts/(?P<pk>\d+)/postnew/', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/postedit/', views.post_edit, name='post_edit'),
    url(r'blog/new', views.blog_new, name='blog_new'),
    url(r'blog/edit', views.blog_edit, name="blog_edit"),
]
