# Generated by Django 3.0.8 on 2020-09-18 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200918_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
    ]
