# Generated by Django 3.0.4 on 2020-06-19 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slm_request_ok',
            name='date_close',
            field=models.DateField(blank=True, null=True),
        ),
    ]
