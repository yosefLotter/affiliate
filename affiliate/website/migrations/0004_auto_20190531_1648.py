# Generated by Django 2.1.7 on 2019-05-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_winner_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lottery',
            name='intro_content',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
