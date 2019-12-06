from django.shortcuts import render
from django.core.cache import cache
from django.views import View
from django.views.generic import View, TemplateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from formtools.preview import FormPreview
from django.urls import reverse_lazy
from .forms import FirstEntryForm, SecondEntryForm
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
    form = FirstEntryForm(request.POST)
        
    join_user = form.save(commit=False)
    join_user.save()

    cache.clear()
        
    url = reverse_lazy('reception:test_success')
    return HttpResponseRedirect(url)

first_entry_form_preview = FirstEntryFormPreview(FirstEntryForm)

# テスト用登録完了画面
class TestSuccess(TemplateView):
  template_name = 'reception/test_success.html'

test_success = TestSuccess.as_view()

# # 参加表入力(初回)確認画面
# class firstFormDetailView():
#   pass
# # 参加表入力(2回目)画面
class SecondFormPreview(FormPreview):
  preview_template = 'reception/second_entry_form_preview.html'
  form_template = 'reception/second_entry_form.html'
  def done(self, request, cleaned_data):
    form = SecondEntryForm(request.POST)

    user = None
    # データベースの内容と一致するかどうか
    try:
      user = JoinUser.objects.get(last_name=form.last_name, first_name=form.first_name, birthday=form.birthday, phone_number=form.phone_number)
    except JoinUser.DoesNotExist:
      print('電話番号での検索ヒットなし')
    try:
      user = JoinUser.objects.get(last_name=form.last_name, first_name=form.first_name, birthday=form.birthday, postal_code=form.postal_code)
    except JoinUser.DoesNotExist:
      print('郵便番号での検索ヒットなし')
    
    if user is None:
      url = reverse_lazy('reception:test_failed')
    else:
      url = reverse_lazy('reception:second_entry_form_detail')
    return HttpResponseRedirect(url)

second_entry_form = SecondFormPreview(SecondEntryForm)

# # 参加表入力(2回目)確認画面
class secondFormDetailView():
  pass

class JoinConfirm(TemplateView):
  template_name = 'reception/join_confirm.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["title"] = "20XX年第N回オープンキャンパス"
    return context

join_confirm = JoinConfirm.as_view()




