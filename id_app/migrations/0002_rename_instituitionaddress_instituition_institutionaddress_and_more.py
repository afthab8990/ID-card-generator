# Generated by Django 5.0 on 2024-10-06 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('id_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionAddress',
            new_name='institutionAddress',
        ),
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionEmail',
            new_name='institutionEmail',
        ),
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionEmail2',
            new_name='institutionEmail2',
        ),
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionLogo',
            new_name='institutionLogo',
        ),
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionName',
            new_name='institutionName',
        ),
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionNumber',
            new_name='institutionNumber',
        ),
        migrations.RenameField(
            model_name='instituition',
            old_name='instituitionNumber2',
            new_name='institutionNumber2',
        ),
    ]
