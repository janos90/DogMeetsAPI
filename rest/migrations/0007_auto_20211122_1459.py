# Generated by Django 3.2.8 on 2021-11-22 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0006_activity_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='lat',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='lng',
            field=models.DecimalField(decimal_places=6, default=0, max_digits=9),
            preserve_default=False,
        ),
    ]
