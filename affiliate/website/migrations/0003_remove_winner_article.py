# Generated by Django 2.1.7 on 2019-05-31 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20190531_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='winner',
            name='article',
        ),
    ]
