# Generated by Django 4.1.7 on 2023-03-08 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0009_job_onwer_alter_apply_cover_letter'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='onwer',
            new_name='owner',
        ),
    ]
