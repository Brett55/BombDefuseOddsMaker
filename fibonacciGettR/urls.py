from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'fibonacciGettR.views.main'),
    url(r'^v1/calculate/(\d+)/(\d+)/(\d+)/$', 'fibonacciGettR.views.calculate'),
    url(r'^v1/calculate_and_save/$', 'fibonacciGettR.views.calculate_and_save')
)