from django.shortcuts import render
from django.views import View
from django.views.generic import View, TemplateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from formtools.preview import FormPreview
from django.urls import reverse_lazy
from .forms import FirstEntryFrom
from .models import JoinUser

# # 初回参加確認画面
# class firstJoinView():
#   pass
# 参加表入力(初回)画面
# class FirstEntryFormView(FormView):
#   model = JoinUser
#   template_name = 'reception/first_entry_form.html'
#   form_class = FirstEntryFrom
#   success_url = reverse_lazy('reception:test_success')
  
# first_entry_form = FirstEntryFormView.as_view()

# フォームと確認画面
class FirstEntryFormPreview(FormPreview):
  preview_template = 'reception/first_entry_form_preview.html'
  form_template = 'reception/first_entry_form.html'
  def done(self, request, cleaned_data):
    form = FirstEntryFrom(request.POST)
        
    join_user = form.save(commit=False)
    join_user.save()
        
    url = reverse_lazy('reception:test_success')
    return HttpResponseRedirect(url)

first_entry_form_preview = FirstEntryFormPreview(FirstEntryFrom)

# テスト用登録完了画面
class TestSuccess(TemplateView):
  template_name = 'reception/test_success.html'

test_success = TestSuccess.as_view()

# # 参加表入力(初回)確認画面
# class firstFormDetailView():
#   pass
# # 参加表入力(2回目)画面
# class secondFormView():
#   pass
# # 参加表入力(2回目)確認画面
# class secondFormDetailView():
#   pass




