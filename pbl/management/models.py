from django.db import models
import datetime

class Department(models.Model):
  class Meta:
    db_table = 'department'
    verbose_name_plural = '学科'

  name = models.CharField(max_length=50, verbose_name='学科名')
  school_year = models.PositiveSmallIntegerField(verbose_name='学年')
  # image_color = models.CharField(max_length=20 ,verbose_name='イメージカラー')
  description = models.TextField(verbose_name='学科概要', max_length=255)
  created = models.DateTimeField(default=datetime.datetime.now, verbose_name='作成日')

  def __str__(self):
    return self.last_name + self.first_name
