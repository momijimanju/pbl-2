from django import forms
from .models import JoinUser
import datetime
import re

# 正規表現
NUMBER_RE = re.compile('^[0-9]+$')
TWO_BYTES_NUMBER_RE = re.compile('[０１２３４５６７８９]+')
UPPER_ALPHABET_RE = re.compile('[Ａ-Ｚ]+')
LOWER_ALPHABET_RE = re.compile('[ａ-ｚ]+')
KATAKANA_RE = re.compile('^[ァ-ンヴー]*$')

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
    }

  def clean_last_name(self):
    last_name = self.cleaned_data['last_name']
    last_name = last_name.replace(' ', '').replace('　', '')
    return last_name
  def clean_first_name(self):
    first_name = self.cleaned_data['first_name']
    first_name = first_name.replace(' ', '').replace('　', '')
    return first_name
  def clean_read_last_name(self):
    read_last_name = self.cleaned_data['read_last_name']
    read_last_name = read_last_name.replace(' ', '').replace('　', '')
    if KATAKANA_RE.match(r'{}'.format(read_last_name)) is None:
      raise forms.ValidationError('カタカナで入力してください')
    return read_last_name
  def clean_read_first_name(self):
    read_first_name = self.cleaned_data['read_first_name']
    read_first_name = read_first_name.replace(' ', '').replace('　', '')
    if KATAKANA_RE.match(r'{}'.format(read_first_name)) is None:
      raise forms.ValidationError('カタカナで入力してください')
    return read_first_name
  def clean_phone_number(self):
    phone_number = self.cleaned_data['phone_number']
    phone_number = phone_number.replace(' ', '').replace('　', '')
    if len(phone_number) < 10:
      raise forms.ValidationError('10桁以上で入力してください')
    if NUMBER_RE.match(r'{}'.format(phone_number)) is None:
      raise forms.ValidationError('半角数字で入力し、記号や全角数字を使用しないでください')
    return phone_number

  def clean_postal_code(self):
    postal_code = self.cleaned_data['postal_code']
    postal_code = postal_code.replace(' ', '').replace('　', '')
    if len(postal_code) < 7:
      raise forms.ValidationError('7桁で入力してください')
    if NUMBER_RE.match(r'{}'.format(postal_code)) is None:
      raise forms.ValidationError('半角数字で入力し、記号や全角数字を使用しないでください')
    return postal_code

  def clean_street_address(self):
    street_address = self.cleaned_data['street_address']
    street_address = street_address.replace(' ', '').replace('　', '')
    if TWO_BYTES_NUMBER_RE.search(r'{}'.format(street_address)) is not None:
      raise forms.ValidationError('半角数字を使用し、全角数字を使用しないでください')
    return street_address
  
  def clean_high_school_name(self):
    high_school_name = self.cleaned_data['high_school_name']
    profession = self.cleaned_data['profession']
    # 学生を選択しているのに空
    if profession == 1:
      if high_school_name is None:
        raise forms.ValidationError('学生を選択している場合必須です')
    return high_school_name

  def clean_school_year(self):
    school_year = self.cleaned_data['school_year']
    profession = self.cleaned_data['profession']
    # 学生を選択しているのに空
    if profession == 1:
      if school_year is None:
        raise forms.ValidationError('いずれかの項目を選択してください')
    return school_year

  def clean_graduation_year(self):
    graduation_year = self.cleaned_data['graduation_year']
    profession = self.cleaned_data['profession']
    # 学生を選択しているのに空
    if profession == 1:
      if graduation_year is None:
        raise forms.ValidationError('いずれかの項目を選択してください')
    return graduation_year



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
      'phone_number': self.fields['phone_number'].help_text,
      'postal_code': self.fields['postal_code'].help_text,
      'street_address': self.fields['street_address'].help_text,
      'high_school_name': self.fields['high_school_name'].help_text,
    }

    # プレースホルダー
    self.fields['last_name'].widget.attrs['placeholder'] = PLACE_HOLDER['last_name']
    self.fields['first_name'].widget.attrs['placeholder'] = PLACE_HOLDER['first_name']
    self.fields['read_last_name'].widget.attrs['placeholder'] = PLACE_HOLDER['read_last_name']
    self.fields['read_first_name'].widget.attrs['placeholder'] = PLACE_HOLDER['read_first_name']
    self.fields['phone_number'].widget.attrs['placeholder'] = PLACE_HOLDER['phone_number']
    self.fields['postal_code'].widget.attrs['placeholder'] = PLACE_HOLDER['postal_code']
    self.fields['street_address'].widget.attrs['placeholder'] = PLACE_HOLDER['street_address']
    self.fields['high_school_name'].widget.attrs['placeholder'] = PLACE_HOLDER['high_school_name']


# 2回目以降参加者入力画面のフォーム
class SecondEntryForm(forms.ModelForm):
  class Meta:
    model = JoinUser
    fields = ('first_name', 'last_name',
               'birthday', 'phone_number', 'postal_code', 
    )
    
    widgets = {
            'birthday': forms.SelectDateWidget(years=[x for x in range(1950, datetime.datetime.now().year + 1)]),
            'gender': forms.RadioSelect,
            'profession': forms.RadioSelect,
    }

  def clean_last_name(self):
    last_name = self.cleaned_data['last_name']
    if last_name is None:
      raise forms.ValidationError('このフィールドを入力してください')
    return last_name
  def clean_first_name(self):
    first_name = self.cleaned_data['first_name']
    if first_name is None:
      raise forms.ValidationError('このフィールドを入力してください')
    return first_name
  def clean_phone_number(self):
    phone_number = self.cleaned_data['phone_number']
    if len(phone_number) < 10:
      raise forms.ValidationError('10桁以上で入力してください')
    if NUMBER_RE.match(r'{}'.format(phone_number)) is None:
      raise forms.ValidationError('半角数字で入力し、記号や全角数字を使用しないでください')
    return phone_number

  def clean_postal_code(self):
    postal_code = self.cleaned_data['postal_code']
    if len(postal_code) < 7:
      raise forms.ValidationError('7桁で入力してください')
    if NUMBER_RE.match(r'{}'.format(postal_code)) is None:
      raise forms.ValidationError('半角数字で入力し、記号や全角数字を使用しないでください')
    return postal_code


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
      'phone_number': self.fields['phone_number'].help_text,
      'postal_code': self.fields['postal_code'].help_text,

    }

    # プレースホルダー
    self.fields['last_name'].widget.attrs['placeholder'] = PLACE_HOLDER['last_name']
    self.fields['first_name'].widget.attrs['placeholder'] = PLACE_HOLDER['first_name']
    self.fields['phone_number'].widget.attrs['placeholder'] = PLACE_HOLDER['phone_number']
    self.fields['postal_code'].widget.attrs['placeholder'] = PLACE_HOLDER['postal_code']
    






