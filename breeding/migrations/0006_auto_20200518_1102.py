# Generated by Django 3.0.6 on 2020-05-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0005_aviary_last_cleaned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='falcon',
            name='CITES_img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='RDOS_permission_img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='photos_old',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='photos_young',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='registration_img',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
