# Generated by Django 2.2.10 on 2020-03-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200319_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='purpose',
            field=models.CharField(choices=[('kaju', 'カジュアル'), ('ランクマッチ', 'ランクマッチ'), ('イベント', 'イベント')], default='kaju', max_length=20),
        ),
    ]
