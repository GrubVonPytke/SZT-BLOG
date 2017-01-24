
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^show_all/$', 'articles.views.articles'),
    url(r'^(?P<article_id>\d+)/$', 'articles.views.article'),
    url(r'^(?P<article_id>\d+)/add_comment/$', 'articles.views.add_comment'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)