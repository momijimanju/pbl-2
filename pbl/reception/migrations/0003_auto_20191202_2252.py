# Generated by Django 2.2.7 on 2019-12-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0002_joinuser_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joinuser',
            name='high_school_name',
            field=models.CharField(default=None, max_length=32, null=True, verbose_name='高校名'),
        ),
    ]