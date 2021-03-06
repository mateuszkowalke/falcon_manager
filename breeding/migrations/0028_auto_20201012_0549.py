# Generated by Django 3.0.7 on 2020-10-12 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0027_auto_20201009_1536'),
    ]

    operations = [
        migrations.CreateModel(
            name='Birth_cert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signature', models.CharField(max_length=16)),
                ('cert_file', models.FileField(blank=True, null=True, upload_to='falcon_docs/')),
            ],
        ),
        migrations.RemoveField(
            model_name='aviary',
            name='falcons',
        ),
        migrations.RemoveField(
            model_name='aviary',
            name='pair',
        ),
        migrations.RemoveField(
            model_name='falcon',
            name='photos_old',
        ),
        migrations.RemoveField(
            model_name='falcon',
            name='photos_young',
        ),
        migrations.AddField(
            model_name='photo',
            name='falcon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='breeding.Falcon'),
        ),
        migrations.AddField(
            model_name='falcon',
            name='birth_cert',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='birth_cert', to='breeding.Birth_cert'),
        ),
    ]
