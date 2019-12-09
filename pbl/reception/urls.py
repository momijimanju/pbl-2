from django.urls import path

from . import views

app_name = 'reception'

urlpatterns = [
  path('firstform/', views.first_entry_form_preview, name='first_entry_form_preview'),
  path('firstform/test_success/', views.test_success, name='test_success'),
  # path('firstform/test_form/', views.first_entry_form, name='first_entry_form_view'),
  # 藤野
  path('secondform/', views.second_entry_form, name='second_entry_form'),
  path('secondform/detail/<int:pk>', views.second_entry_detail, name='second_entry_detail'),
  path('secondform/update/<int:pk>', views.second_entry_update, name='second_entry_update'),
  # シラガ
  path('join/', views.join_confirm, name='join_confirm'),
]