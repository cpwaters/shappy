# Generated by Django 3.2.6 on 2021-08-31 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='pub_date',
        ),
    ]
