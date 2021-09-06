# Generated by Django 3.0.2 on 2021-09-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=128, verbose_name='artist')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('price', models.IntegerField(verbose_name='price')),
                ('country', models.CharField(max_length=128, verbose_name='country')),
                ('released', models.CharField(max_length=128, verbose_name='released')),
                ('genre', models.CharField(max_length=128, verbose_name='genre')),
            ],
        ),
    ]