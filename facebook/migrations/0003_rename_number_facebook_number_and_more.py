# Generated by Django 5.0.7 on 2024-07-19 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0002_alter_facebook_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facebook',
            old_name='number',
            new_name='Number',
        ),
        migrations.RenameField(
            model_name='facebook',
            old_name='password',
            new_name='Password',
        ),
    ]
