from django.urls import path

from . import views

app_name = 'reception'

urlpatterns = [
  path('firstform/', views.first_entry_form, name='first_entry_form')
]