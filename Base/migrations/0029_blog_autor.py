# Generated by Django 4.2.7 on 2023-12-22 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0028_rename_instrumento_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='autor',
            field=models.CharField(default='', max_length=200),
        ),
    ]
