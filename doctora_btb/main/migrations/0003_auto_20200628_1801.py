# Generated by Django 3.0.3 on 2020-06-28 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_message_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='error',
            field=models.TextField(default='NULL', verbose_name='Ошибка отправки'),
        ),
    ]
