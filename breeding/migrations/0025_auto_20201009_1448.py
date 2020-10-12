# Generated by Django 3.0.7 on 2020-10-09 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('breeding', '0024_auto_20201009_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='falcon',
            name='father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='breeding.Falcon'),
        ),
        migrations.AlterField(
            model_name='falcon',
            name='mother',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='breeding.Falcon'),
        ),
        migrations.RemoveField(
            model_name='falcon',
            name='youngsters',
        ),
        migrations.AddField(
            model_name='falcon',
            name='youngsters',
            field=models.ManyToManyField(blank=True, null=True, related_name='_falcon_youngsters_+', to='breeding.Falcon'),
        ),
    ]
