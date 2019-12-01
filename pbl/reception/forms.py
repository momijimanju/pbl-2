from django import forms
from .models import JoinUser
import datetime

# 初回参加者入力画面のフォーム
class FirstEntryFrom(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # 郵便番号を入力すると住所を自動的に入力するための属性指定
    self.fields['postal_code'].widget = forms.TextInput(attrs={
      'onKeyUp': "AjaxZip3.zip2addr(this,'','street_address','street_address');",
    })
    # self.fields['street_address'].widget.attrs['readonly'] = True
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'

  class Meta:
    model = JoinUser
    fields = ('first_name', 'last_name','read_first_name', 'read_last_name',
               'birthday', 'gender', 'phone_number', 'postal_code', 'street_address', 
               'profession', 'school_year', 'graduation_year', 'graduate', 'certification',
               'high_school_name',
             )
    
    widgets = {
            'birthday': forms.SelectDateWidget(years=[x for x in range(1950, datetime.datetime.now().year + 1)]),
            'gender': forms.RadioSelect,
            'profession': forms.RadioSelect,
    }

