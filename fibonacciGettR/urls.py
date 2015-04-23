from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'fibonacciGettR.views.main'),
    url(r'^calculate/v1/(\d+)/$', 'fibonacciGettR.views.calculate')
)