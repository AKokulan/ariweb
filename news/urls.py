from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from news import views as news_view

urlpatterns = [
    path('',news_view.show_home,name='show_home')
]

urlpatterns += staticfiles_urlpatterns()