# Generated by Django 3.0.8 on 2020-09-18 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
    ]
