# Generated by Django 3.0.8 on 2020-07-01 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='craeted_at',
            new_name='created_at',
        ),
    ]
