# Generated by Django 3.2.8 on 2021-11-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0004_rename_organiser_id_activity_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='name',
            field=models.CharField(default='tempname', max_length=255),
            preserve_default=False,
        ),
    ]
