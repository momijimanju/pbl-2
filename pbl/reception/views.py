from django.shortcuts import render
from django.core.cache import cache
from django.views import View
from django.views.generic import View, TemplateView, FormView, DetailView, UpdateView
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
    print(cleaned_data['last_name'])

    user = None
    # データベースの内容と一致するかどうか
    try:
      user = JoinUser.objects.get(last_name=cleaned_data['last_name'], first_name=cleaned_data['first_name'], birthday=cleaned_data['birthday'], phone_number=cleaned_data['phone_number'])
    except JoinUser.DoesNotExist:
      print('電話番号での検索ヒットなし')
    try:
      user = JoinUser.objects.get(last_name=cleaned_data['last_name'], first_name=cleaned_data['first_name'], birthday=cleaned_data['birthday'], postal_code=cleaned_data['postal_code'])
    except JoinUser.DoesNotExist:
      print('郵便番号での検索ヒットなし')
    
    if user is None:
      url = reverse_lazy('reception:test_failed')
    else:
      url = reverse_lazy('reception:second_entry_detail', kwargs={'pk': user.id})
    return HttpResponseRedirect(url)

second_entry_form = SecondFormPreview(SecondEntryForm)

# # 参加表入力(2回目)確認画面
class SecondEntryDetailView(DetailView):
  model = JoinUser
  template_name = 'reception/second_entry_detail.html'

second_entry_detail = SecondEntryDetailView.as_view()

class SecondEntryUpdateView(UpdateView):
  model = JoinUser
  form_class = FirstEntryForm
  template_name = 'reception/second_entry_update.html'

  def get_success_url(self):
    return reverse_lazy('reception:second_entry_detail', kwargs={'pk': self.kwargs['pk']})
  
  def form_valid(self, form):
    join_user = form.save(commit=False)
    # ラジオボタンくん保存されてくれーーーーー
    join_user.gender = form.cleaned_data['gender']
    join_user.profession = form.cleaned_data['profession']
    join_user.save()
    return super().form_valid(form)

second_entry_update = SecondEntryUpdateView.as_view()

class JoinConfirm(TemplateView):
  template_name = 'reception/join_confirm.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["title"] = "20XX年第N回オープンキャンパス"
    return context

join_confirm = JoinConfirm.as_view()




