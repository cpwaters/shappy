# Generated by Django 3.2.6 on 2021-09-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricelist', '0006_product_pack_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.CharField(default='Aldi', max_length=50),
        ),
    ]