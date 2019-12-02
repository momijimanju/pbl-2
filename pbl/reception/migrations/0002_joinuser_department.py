# Generated by Django 2.2.7 on 2019-12-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reception', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinuser',
            name='department',
            field=models.PositiveSmallIntegerField(choices=[(1, '医療福祉事務学科'), (2, '診療情報管理士学科'), (3, 'ホテル・ブライダル学科'), (4, '経営アシスト学科'), (5, '公務員・公務員速修学科'), (6, '保育学科'), (7, '情報スペシャリスト学科'), (8, '情報システム学科'), (9, 'ゲームクリエイター・ゲームプログラマー学科'), (10, 'データマーケター学科'), (11, 'ネット・動画クリエイター学科'), (12, 'CGデザイン学科')], default=1, verbose_name='参加希望学科'),
        ),
    ]