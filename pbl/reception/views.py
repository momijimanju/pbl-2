from django.shortcuts import render
from django.views import View
from django.views.generic import View, TemplateView, CreateView
from .forms import FirstEntryFrom
from .models import JoinUser

# # 初回参加確認画面
# class firstJoinView():
#   pass
# # 参加表入力(初回)画面
class FirstEntryFormView(CreateView):
  model = JoinUser
  template_name = 'reception/first_entry_form.html'
  form_class = FirstEntryFrom
  
first_entry_form = FirstEntryFormView.as_view()
# # 参加表入力(初回)確認画面
# class firstFormDetailView():
#   pass
# # 参加表入力(2回目)画面
# class secondFormView():
#   pass
# # 参加表入力(2回目)確認画面
# class secondFormDetailView():
#   pass




