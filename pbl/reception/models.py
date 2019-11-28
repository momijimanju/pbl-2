from django.db import models

class JoinUser(models.Model):
  class Meta:
    db_table = 'join_user'
    verbose_name_plural = "参加ユーザー"

  last_name = models.CharField(verbose_name='苗字', max_length=8)
  first_name = models.CharField(verbose_name='名前', max_length=32)
  read_last_name = models.CharField(verbose_name='苗字フリガナ', max_length=16)
  read_first_name = models.CharField(verbose_name='名前フリガナ', max_length=32)
  birthday = models.DateField(verbose_name='生年月日')
  gender = models.PositiveSmallIntegerField(verbose_name='性別', help_text="1:女性, 2:男性, 3:未回答", default=3)
  phone_number_regex = RegexValidator(regex = r'^[0-9]+$', message = ("ハイフンなし電話番号が入力されていないときのエラーメッセージを入力"))
  phone_number = models.CharField(validators = [phone_number_regex],verbose_name='電話番号(ハイフンなし)', max_length=11)
  postal_code_regex = RegexValidator(regex = r'^[0-9]+$', message = ("ハイフンなし郵便番号が入力されていない時のエラーメッセージ"))
  postal_code = models.CharField(validators = [postal_code_regex],verbose_name='郵便番号(ハイフンなし)', max_length=7)
  street_address = models.CharField(verbose_name='住所', max_length=64)
  profession = models.PositiveSmallIntegerField(verbose_name= '職業', help_text="1:学生,2:その他",default=1)
  high_school_id = models.IntegerField(verbose_name='高校ID',max_length=4,blank=True,default=null)
  school_year = models.IntegerField(verbose_name='学年',max_length=1,blank=True,default=null)
  graduation_year = models.IntegerField(verbose_name='卒業年度',max_length=4,blank=True,default=null)
  


  def __str__(self):
    return self.last_name + self.first_name