# Generated by Django 3.0.2 on 2020-02-03 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TRDWLL', '0004_auto_20200203_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='url',
            field=models.URLField(blank=True, help_text='Display the alert on a specified page.', null=True),
        ),
    ]
