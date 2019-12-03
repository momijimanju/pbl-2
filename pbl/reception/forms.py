from django import forms
from .models import JoinUser
import datetime

# 初回参加者入力画面のフォーム
class FirstEntryForm(forms.ModelForm):
  class Meta:
    model = JoinUser
    fields = ('first_name', 'last_name','read_first_name', 'read_last_name',
               'birthday', 'gender', 'phone_number', 'postal_code', 'street_address', 
               'profession', 'school_year', 'graduation_year', 'graduate', 'certification',
               'high_school_name', 'department',
    )
    
    widgets = {
            'birthday': forms.SelectDateWidget(years=[x for x in range(1950, datetime.datetime.now().year + 1)]),
            'gender': forms.RadioSelect,
            'profession': forms.RadioSelect,
    }

  def clean_postal_code(self):
    postal_code = self.cleaned_data['postal_code']
    if len(postal_code) < 7:
      raise forms.ValidationError('7桁で入力してください')
    return postal_code
  
  def clean_high_school_name(self):
    high_school_name = self.cleaned_data['high_school_name']
    profession = self.cleaned_data['profession']
    # 学生を選択しているのに高校名が空
    if profession == 1:
      if high_school_name == '':
        raise forms.ValidationError('このフィールドを入力してください')
    return high_school_name



  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    # 郵便番号を入力すると住所を自動的に入力するための属性指定
    self.fields['postal_code'].widget.attrs['onKeyUp'] = "AjaxZip3.zip2addr(this,'','street_address','street_address');"
    # self.fields['street_address'].widget.attrs['readonly'] = True
    for field in self.fields.values():
      field.widget.attrs['class'] = 'form-control'

    PLACE_HOLDER = {
      'last_name': '二宮',
      'first_name': '一馬',
      'read_last_name': 'ニノミヤ',
      'read_first_name': 'カズマ',
      'phone_number': self.fields['phone_number'].help_text
    }

    # プレースホルダー
    self.fields['last_name'].widget.attrs['placeholder'] = PLACE_HOLDER['last_name']
    self.fields['first_name'].widget.attrs['placeholder'] = PLACE_HOLDER['first_name']
    self.fields['read_last_name'].widget.attrs['placeholder'] = PLACE_HOLDER['read_last_name']
    self.fields['read_first_name'].widget.attrs['placeholder'] = PLACE_HOLDER['read_first_name']
    self.fields['phone_number'].widget.attrs['placeholder'] = PLACE_HOLDER['phone_number']



