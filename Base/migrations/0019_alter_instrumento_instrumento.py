# Generated by Django 4.2.7 on 2023-12-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0018_alter_instrumento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumento',
            name='instrumento',
            field=models.CharField(choices=[('guitarra', 'Guitarra'), ('bajo', 'Bajo'), ('pedal', 'Pedal'), ('bateria', 'Bateria'), ('teclado', 'Teclado'), ('amplificador', 'Amplificador'), ('otro', 'Otro')], default='guitarra', max_length=15),
        ),
    ]
