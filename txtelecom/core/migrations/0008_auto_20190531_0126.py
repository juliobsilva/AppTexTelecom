# Generated by Django 2.0 on 2019-05-31 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190531_0121'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrecoDois',
        ),
        migrations.DeleteModel(
            name='PrecoTres',
        ),
        migrations.RenameField(
            model_name='precoum',
            old_name='preco_um',
            new_name='preco',
        ),
    ]
