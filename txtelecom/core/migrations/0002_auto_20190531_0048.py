# Generated by Django 2.0 on 2019-05-31 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='precoum',
            name='preco',
            field=models.IntegerField(verbose_name='Preco Um'),
        ),
    ]