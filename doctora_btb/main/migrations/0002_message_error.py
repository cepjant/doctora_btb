# Generated by Django 3.0.3 on 2020-06-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='error',
            field=models.CharField(default='NULL', max_length=50, verbose_name='Ошибка отправки'),
        ),
    ]
