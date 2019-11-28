from django.urls import path

from . import views

app_name = 'reception'

urlpatterns = [
  path('firstform/', views.first_entry_form, name='first_entry_form'),
  # path('firstform/detail', views.first_entry_form_detail, name='first_entry_form_detail'),
  # path('secondform/', views.second_entry_form, name='second_entry_form'),
  # path('secondform/detail', views.second_entry_form_detail, name='second_entry_form_detail'),
  # path('joinconfirm/', views.join_confirm, name='join_confirm'),
]