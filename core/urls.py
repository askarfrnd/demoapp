"""core URL Configuration

The `urlpatterns` list routes URLs to core views.
"""

from django.conf.urls import url

from .views import HomePage, WelcomePage, LogView


urlpatterns = [
    url(r'^$', HomePage.as_view(template_name='index.html')),
    url(r'^welcome/$', WelcomePage.as_view(), name='welcome_page'),
    url(r'^log/$', LogView.as_view(), name='log_api')
]