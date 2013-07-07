from django.conf.urls.defaults import *
from models import Entry, Tag
from django.views.generic.dates import ArchiveIndexView, DateDetailView
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^/?$', ArchiveIndexView.as_view(model=Entry, date_field="published_on"), name="news-main"),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[0-9A-Za-z-]+)/$', 'date_based.object_detail', dict(entry_dict, slug_field='slug', month_format='%m'),name="news-detail"),
    url(r'^(?P<year>\d+)/(?P<month>[-\w]+)/(?P<day>\d+)/(?P<pk>\d+)/$',
        DateDetailView.as_view(model=Entry, date_field="published_on"),
        name="news_detail"),
    url(r'^about/$', TemplateView.as_view(template_name='news/about.html'), name='news-about'),
)


