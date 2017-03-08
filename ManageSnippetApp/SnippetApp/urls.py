# SnippetApp/urls.py
from django.conf.urls import url, include
from SnippetApp import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]