# Generated by Django 2.2 on 2019-05-22 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lottery', models.CharField(max_length=100)),
                ('first_title', models.CharField(blank=True, max_length=100)),
                ('first_content', models.TextField(blank=True)),
                ('second_title', models.CharField(blank=True, max_length=100)),
                ('second_content', models.TextField(blank=True)),
                ('third_title', models.CharField(blank=True, max_length=100)),
                ('third_content', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
