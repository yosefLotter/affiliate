# Generated by Django 2.2 on 2019-07-13 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20190711_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottery_supplier',
            name='content_box_4',
        ),
        migrations.RemoveField(
            model_name='winner',
            name='youtube_link',
        ),
        migrations.AddField(
            model_name='lottery_supplier',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
