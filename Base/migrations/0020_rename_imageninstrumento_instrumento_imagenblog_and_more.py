# Generated by Django 4.2.7 on 2023-12-21 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0019_alter_instrumento_instrumento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instrumento',
            old_name='imagenInstrumento',
            new_name='imagenBlog',
        ),
        migrations.AlterField(
            model_name='instrumento',
            name='instrumento',
            field=models.CharField(choices=[('blog', 'Blog')], default='blog', max_length=15),
        ),
    ]