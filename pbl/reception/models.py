from django.db import models

class JoinUser(models.Model):
  class Meta:
    db_table = 'join_user'
    verbose_name_plural = "参加ユーザー"

  first_name = models.CharField(verbose_name='名前', max_length=20)
  last_name = models.CharField(verbose_name='名字', max_length=20)
  read_first_name = models.CharField(verbose_name='名前(フリガナ)', max_length=20)
  read_last_name = models.CharField(verbose_name='名字(フリガナ)', max_length=20)
  birthday = models.DateField(verbose_name='生年月日')
  gender = models.PositiveSmallIntegerField(verbose_name="性別", help_text="1:女性, 2:男性, 3:未回答", default=3)
  phone_number = models.CharField(verbose_name='電話番号(ハイフンなし)', max_length=20)
  postal_code = models.CharField(verbose_name='電話番号(ハイフンなし)', max_length=20)


  def __str__(self):
    return self.last_name + self.first_name