# Generated by Django 2.2.10 on 2020-03-19 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200319_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='purpose',
            field=models.CharField(choices=[('カジュアル', 'カジュアル'), ('ランクマッチ', 'ランクマッチ'), ('イベント', 'イベント')], default='kaju', max_length=20),
        ),
    ]
