# Generated by Django 3.0.4 on 2020-04-18 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TRDWLL', '0007_auto_20200203_0343'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name': 'About', 'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='alert',
            options={'ordering': ['type'], 'verbose_name': 'Alert', 'verbose_name_plural': 'Alerts'},
        ),
    ]
