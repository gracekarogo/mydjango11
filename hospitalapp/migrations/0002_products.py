# Generated by Django 5.0.2 on 2024-02-26 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.CharField(max_length=100)),
                ('product_quantity', models.CharField(max_length=100)),
            ],
        ),
    ]
