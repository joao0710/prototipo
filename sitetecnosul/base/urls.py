from django.urls import path

from sitetecnosul.base.views import home

app_name='base'
urlpatterns = [
    path('', home, name='home'),
]