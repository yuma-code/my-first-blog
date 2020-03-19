# Generated by Django 2.2.10 on 2020-03-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='psid',
        ),
        migrations.AlterField(
            model_name='post',
            name='device',
            field=models.CharField(choices=[('PS4', 'PS4'), ('PC', 'PC')], default='PS4', max_length=20),
        ),
    ]
