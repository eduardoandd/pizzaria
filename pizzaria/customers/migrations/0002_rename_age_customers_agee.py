# Generated by Django 3.2.4 on 2024-11-16 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customers',
            old_name='Age',
            new_name='Agee',
        ),
    ]