# Generated by Django 3.2.13 on 2022-05-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assessments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessment',
            old_name='registrant',
            new_name='registrar',
        ),
    ]