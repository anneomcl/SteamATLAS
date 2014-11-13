from django.conf.urls import patterns, url
from django.conf import settings

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^recommend/(?P<tag>\w+)/$', views.recommend, name = 'game_recommended'),
    # ex: /polls/5/
    #url(r'^(?P<app_ID>\d+)/$', views.detail, name='detail'),
    #ex: /polls/tag_results/
    url(r'^tag_results/', views.tag_results, name ='tag_results')
)

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))

'''urlpatterns += patterns('',
                        (r'^polls/media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))'''

'''urlpatterns += patterns('',
                        (r'^(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT}))'''