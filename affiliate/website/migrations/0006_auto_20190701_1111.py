# Generated by Django 2.2 on 2019-07-01 11:11

from django.db import migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190701_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottery',
            name='project_code',
        ),
        migrations.AddField(
            model_name='lottery',
            name='content',
            field=django_bleach.models.BleachField(default=1),
            preserve_default=False,
        ),
    ]