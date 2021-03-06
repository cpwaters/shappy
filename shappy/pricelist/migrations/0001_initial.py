# Generated by Django 3.2.6 on 2021-08-31 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_text', models.CharField(max_length=10)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_text', models.CharField(max_length=200)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricelist.code')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_text', models.CharField(max_length=200)),
                ('code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pricelist.code')),
            ],
        ),
    ]
