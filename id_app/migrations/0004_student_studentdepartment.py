# Generated by Django 5.0 on 2024-10-16 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('id_app', '0003_student_sinstitution'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='studentDepartment',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
