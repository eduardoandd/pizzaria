# Generated by Django 3.2.4 on 2024-11-18 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders_mongo', '0002_auto_20241117_2006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermongo',
            old_name='Product',
            new_name='Products',
        ),
    ]