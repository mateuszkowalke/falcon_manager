# Generated by Django 3.0.7 on 2020-06-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0013_falcon_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='falcon',
            name='additional_info',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
