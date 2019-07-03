# Generated by Django 2.2 on 2019-07-03 15:53

from django.db import migrations, models
import django.db.models.deletion
import django_bleach.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('efter_name', models.CharField(blank=True, max_length=15)),
                ('email_adress', models.CharField(blank=True, max_length=50)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lottery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name_of_lottery', models.CharField(max_length=100)),
                ('continent', models.CharField(max_length=100)),
                ('jackpot', models.CharField(blank=True, max_length=40)),
                ('odds', models.CharField(blank=True, max_length=100)),
                ('dragnings_datum', models.CharField(max_length=400)),
                ('pris_biljett', models.CharField(blank=True, max_length=100)),
                ('intro_content', models.TextField(blank=True, max_length=500)),
                ('logo', models.ImageField(blank=True, default=None, upload_to='')),
                ('mini_content', models.CharField(blank=True, max_length=100)),
                ('welcome_text', django_bleach.models.BleachField(blank=True)),
                ('a_title', models.CharField(blank=True, max_length=200)),
                ('a_content', django_bleach.models.BleachField(blank=True)),
                ('a_content_image_right', models.ImageField(blank=True, default=None, upload_to='')),
                ('b_title', models.CharField(blank=True, max_length=200)),
                ('b_content', django_bleach.models.BleachField(blank=True)),
                ('b_image', models.ImageField(blank=True, default=None, upload_to='')),
                ('c_title', models.CharField(blank=True, max_length=200)),
                ('c_content', django_bleach.models.BleachField(blank=True)),
                ('d_title', models.CharField(blank=True, max_length=200)),
                ('d_content', django_bleach.models.BleachField(blank=True)),
                ('e_title', models.CharField(blank=True, max_length=200)),
                ('e_content', django_bleach.models.BleachField(blank=True)),
                ('f_title', models.CharField(blank=True, max_length=200)),
                ('f_content', django_bleach.models.BleachField(blank=True)),
                ('g_title', models.CharField(blank=True, max_length=200)),
                ('g_content', django_bleach.models.BleachField(blank=True)),
                ('h_title', models.CharField(blank=True, max_length=200)),
                ('h_content', django_bleach.models.BleachField(blank=True)),
                ('i_title', models.CharField(blank=True, max_length=200)),
                ('i_content', django_bleach.models.BleachField(blank=True)),
                ('j_title', models.CharField(blank=True, max_length=200)),
                ('j_content', django_bleach.models.BleachField(blank=True)),
                ('k_title', models.CharField(blank=True, max_length=200)),
                ('k_content', django_bleach.models.BleachField(blank=True)),
                ('l_title', models.CharField(blank=True, max_length=200)),
                ('l_content', django_bleach.models.BleachField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('amount_they_won', models.CharField(blank=True, max_length=400)),
                ('profil_bild', models.ImageField(blank=True, default=None, upload_to='')),
                ('welcome_title', models.CharField(blank=True, max_length=100)),
                ('welcome_text', models.TextField(blank=True)),
                ('a_title', models.CharField(blank=True, max_length=200)),
                ('a_content', models.TextField(blank=True)),
                ('b_title', models.CharField(blank=True, max_length=200)),
                ('b_content', models.TextField(blank=True)),
                ('b_image', models.ImageField(blank=True, default=None, upload_to='')),
                ('c_title', models.CharField(blank=True, max_length=200)),
                ('c_content', models.TextField(blank=True)),
                ('d_title', models.CharField(blank=True, max_length=200)),
                ('d_content', models.TextField(blank=True)),
                ('e_title', models.CharField(blank=True, max_length=200)),
                ('e_content', models.TextField(blank=True)),
                ('bild', models.ImageField(blank=True, default=None, upload_to='')),
                ('youtube_link', models.TextField(blank=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('lottery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Lottery')),
            ],
        ),
    ]
