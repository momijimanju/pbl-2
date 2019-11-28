from django import forms
from .models import JoinUser
import datetime

# 初回参加者入力画面のフォーム
class FirstEntryFrom(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'

  class Meta:
    model = JoinUser
    fields = ('first_name', 'last_name','read_first_name', 'read_last_name',
               'birthday', 'gender', 'phone_number', 'postal_code')
    
    widgets = {
            'birthday': forms.SelectDateWidget(years=[x for x in range(1950, datetime.datetime.now().year + 1)]),
            'gender': forms.RadioSelect
    }

