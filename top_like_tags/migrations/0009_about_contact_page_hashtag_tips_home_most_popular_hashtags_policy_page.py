# Generated by Django 3.0.6 on 2020-06-19 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_like_tags', '0008_analytics'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('keywords', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='contact_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('keywords', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='hashtag_tips',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('keywords', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('keywords', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='most_popular_hashtags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('keywords', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='policy_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000)),
                ('keywords', models.CharField(max_length=3000)),
            ],
        ),
    ]