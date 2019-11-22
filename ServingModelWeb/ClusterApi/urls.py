
from ClusterApi.views import Train, Predict
from django.conf.urls import url

app_name = 'ClusterApi'

urlpatterns = [
    url(r'^train/$', Train.as_view(), name="train"),
    url(r'^predict/$', Predict.as_view(), name="predict"),
]