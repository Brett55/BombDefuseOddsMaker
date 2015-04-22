from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'fibonacciGettR.views.test')
)