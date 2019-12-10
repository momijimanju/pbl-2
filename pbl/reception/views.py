from django.shortcuts import render
from django.core.cache import cache
from django.views import View
from django.views.generic import View, TemplateView, FormView, DetailView, UpdateView
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from formtools.preview import FormPreview
from django.urls import reverse_lazy, reverse
from .forms import FirstEntryForm, SecondEntryForm
from .models import JoinUser

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

class SecondEntryFormView(TemplateView):
  template_name = 'reception/second_entry_form.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["form"] = SecondEntryForm()
    return context

second_entry_form = SecondEntryFormView.as_view()

def search_ajax(request):
  form = SecondEntryForm(request.POST)
  user = None
  data = {
    'db_search': 'None',
    'db_valid_check': 'None',
    'response_url': 'None',
  }
  if form.is_valid():
    form_data = {
      'last_name': request.POST.get("last_name"),
      'first_name': request.POST.get("first_name"),
      'birthday': f'{request.POST.get("birthday_year")}-{request.POST.get("birthday_month")}-{request.POST.get("birthday_day")}',
      'phone_number': request.POST.get("phone_number"),
      'postal_code': request.POST.get("postal_code"),
    }
    data['db_valid_check'] = 'True'
    # データベースの内容と一致するかどうか
    try:
      user = JoinUser.objects.get(last_name=form_data['last_name'], first_name=form_data['first_name'], birthday=form_data['birthday'], phone_number=form_data['phone_number'])
    except JoinUser.DoesNotExist:
      print('電話番号での検索ヒットなし')
    try:
      user = JoinUser.objects.get(last_name=form_data['last_name'], first_name=form_data['first_name'], birthday=form_data['birthday'], postal_code=form_data['postal_code'])
    except JoinUser.DoesNotExist:
      print('郵便番号での検索ヒットなし')
    
    if user is None:
      data['db_search'] = 'False'
    else:
      data['db_search'] = 'True'
      data['response_url'] = reverse('reception:second_entry_detail', kwargs={'pk': user.id})
  else:
    data['db_valid_check'] = 'False'
  return JsonResponse(data)  
  



