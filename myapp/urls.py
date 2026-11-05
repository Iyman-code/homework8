from django.urls import path
from .views import manual_form_view

urlpatterns = [
    path('', manual_form_view, name='manual_form'),
]
