from django.urls import path

from . import views

app_name = 'reception'

urlpatterns = [
  # 初回参加
  path('firstform/', views.first_entry_form_preview, name='first_entry_form_preview'),
  path('firstform/test_success/', views.test_success, name='test_success'),
  # 二回目以降
  path('secondform/', views.second_entry_form, name='second_entry_form'),
  path('secondform/detail/<int:pk>', views.second_entry_detail, name='second_entry_detail'),
  path('secondform/update/<int:pk>', views.second_entry_update, name='second_entry_update'),
  # ajax用
  path('secondform/search_ajax', views.search_ajax, name='search_ajax'),
  # 選択画面
  path('', views.join_confirm, name='join_confirm'),
]