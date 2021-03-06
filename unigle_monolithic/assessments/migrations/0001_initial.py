# Generated by Django 3.2.13 on 2022-05-07 13:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('presents', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='rate')),
                ('comment', models.TextField(verbose_name='comment')),
                ('present', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presents.present', verbose_name='presenting lesson')),
                ('registrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='registrant')),
            ],
            options={
                'verbose_name': 'assessment',
                'verbose_name_plural': 'assessments',
            },
        ),
    ]
