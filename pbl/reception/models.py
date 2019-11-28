from django.db import models
from django.core.validators import RegexValidator

class JoinUser(models.Model):
  class Meta:
    db_table = 'join_user'
    verbose_name_plural = "参加ユーザー"

  GENDER_CHOICE = (('1','男性'),('2','女性'))
  PROFESSION_CHOICE = (('1','学生'),('2','その他'))

  last_name = models.CharField(verbose_name='苗字', max_length=8)
  first_name = models.CharField(verbose_name='名前', max_length=32)
  read_last_name = models.CharField(verbose_name='苗字フリガナ', max_length=16)
  read_first_name = models.CharField(verbose_name='名前フリガナ', max_length=32)
  birthday = models.DateField(verbose_name='生年月日')
  gender = models.PositiveSmallIntegerField(verbose_name='性別',default=1,choices=GENDER_CHOICE)
  phone_number_regex = RegexValidator(regex=r'^[0-9]+$', message=("ハイフンなし電話番号が入力されていないときのエラーメッセージを入力"))
  phone_number = models.CharField(validators = [phone_number_regex],verbose_name='電話番号', max_length=11,help_text='※ハイフン無しで入力してください')
  postal_code_regex = RegexValidator(regex=r'^[0-9]+$', message=("ハイフンなし郵便番号が入力されていない時のエラーメッセージ"))
  postal_code = models.CharField(validators = [postal_code_regex],verbose_name='郵便番号', max_length=7,help_text='※ハイフン無しで入力してください')
  street_address = models.CharField(verbose_name='住所', help_text='※郵便番号を入力することで自動で入力されます',max_length=64)
  address = models.CharField(verbose_name='番地',max_length=20)
  profession = models.PositiveSmallIntegerField(verbose_name='職業',default=1,choices=PROFESSION_CHOICE)
  high_school_id = models.IntegerField(verbose_name='高校ID',blank=True,default=None)
  school_year = models.IntegerField(verbose_name='学年',blank=True,default=None)
  graduation_year = models.IntegerField(verbose_name='卒業予定年',blank=True,default=None)
  graduate = models.PositiveSmallIntegerField(verbose_name='高校卒業済み',blank=True,default=None)
  certification = models.PositiveSmallIntegerField(verbose_name='高認取得済み',blank=True,default=None)
  transportation_count = models.PositiveSmallIntegerField(verbose_name='交通費支給残回数')
  join_count = models.IntegerField(verbose_name='参加回数')
  examinee_join_count =models.IntegerField(verbose_name='受験対象年度参加回数')


  def __str__(self):
    return self.last_name + self.first_name