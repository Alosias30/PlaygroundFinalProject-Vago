# Generated by Django 4.2.7 on 2023-12-22 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0024_alter_instrumento_instrumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrumento',
            name='direccion',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
