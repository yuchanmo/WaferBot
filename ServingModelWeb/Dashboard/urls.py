from django.urls import path
import Dashboard.views as views

app_name = 'DashBoard'

urlpatterns = [
    path('',views.index,name='index')]
