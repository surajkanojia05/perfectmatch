# Generated by Django 3.2.6 on 2021-09-28 06:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0002_auto_20210927_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='tag',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
