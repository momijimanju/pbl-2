from django.shortcuts import render
from django.views import View
from django.views.generic import View, TemplateView, CreateView, DetailView
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
# class ProblemGroupDetailView(DetailView):
#     template_name = "triplefour/problem/group/detail.html"
#     model = JoinUser

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # context['preblem_group'] = QuestionGroup.objects.filter(id=self.kwargs['pk'])
        
#         context['problem_group'] = JoinUser.objects.get(id=self.kwargs['pk'])
#         return context
# # 参加表入力(初回)確認画面
# class firstFormDetailView(DetailView):
#   pass
# # 参加表入力(2回目)画面
# class secondFormView(CreateView):
#   pass
# # 参加表入力(2回目)確認画面
# class secondFormDetailView(DetailView):
#   pass




