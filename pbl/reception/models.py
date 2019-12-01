from django.db import models
from django.core.validators import RegexValidator
import datetime

class JoinUser(models.Model):
  class Meta:
    db_table = 'join_user'
    verbose_name_plural = "参加ユーザー"

  GENDER_CHOICE = ((1,'男性'), (2,'女性'))
  PROFESSION_CHOICE = ((1,'学生'), (2,'その他'))
  SCHOOL_YEAR_CHOICE = ((1, '1年'), (2, '2年'), (3, '3年'), (4, '4年'))
  GRADUATION_YEAR_CHOICES = []
  for r in range(datetime.datetime.now().year, (datetime.datetime.now().year + 11)):
    GRADUATION_YEAR_CHOICES.append((r,r))

  last_name = models.CharField(verbose_name='名字', max_length=8)
  first_name = models.CharField(verbose_name='名前', max_length=32)
  read_last_name = models.CharField(verbose_name='名字(カナ)', max_length=16)
  read_first_name = models.CharField(verbose_name='名前(カナ)', max_length=32)
  birthday = models.DateField(verbose_name='生年月日')
  gender = models.PositiveSmallIntegerField(verbose_name='性別',default=1,choices=GENDER_CHOICE)
  phone_number = models.CharField(verbose_name='電話番号', max_length=11, help_text='※ハイフン無しで入力してください')
  postal_code = models.CharField(verbose_name='郵便番号', max_length=7, help_text='※ハイフン無しで入力してください')
  street_address = models.CharField(verbose_name='住所', help_text='※郵便番号を入力することで市町村までが自動で入力されます',max_length=64)
  profession = models.PositiveSmallIntegerField(verbose_name='職業',default=1,choices=PROFESSION_CHOICE)
  high_school_name = models.CharField(verbose_name='高校名',blank=True, max_length=32, default=None)
  school_year = models.PositiveSmallIntegerField(verbose_name='学年', choices=SCHOOL_YEAR_CHOICE, default=None)
  graduation_year = models.IntegerField(verbose_name='卒業予定年',choices=GRADUATION_YEAR_CHOICES, default=None)
  graduate = models.NullBooleanField(verbose_name='高校卒業済み',blank=True, default=None)
  certification = models.NullBooleanField(verbose_name='高認取得済み',blank=True, default=None)
  # transportation_count = models.PositiveSmallIntegerField(verbose_name='交通費支給残回数')
  # join_count = models.IntegerField(verbose_name='参加回数')
  # examinee_join_count =models.IntegerField(verbose_name='受験対象年度参加回数')
  created = models.DateTimeField(default=datetime.datetime.now, verbose_name="作成日")


  def __str__(self):
    return self.last_name + self.first_name