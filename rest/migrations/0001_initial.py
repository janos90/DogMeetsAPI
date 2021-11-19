# Generated by Django 3.2.7 on 2021-10-06 12:31

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/owners')),
                ('phone', models.CharField(max_length=20)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('breed', models.CharField(max_length=255)),
                ('height', models.CharField(max_length=255)),
                ('weight', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('anniversary', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/dog-profiles')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.owner')),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('startTime', models.DateTimeField()),
                ('dogs', models.ManyToManyField(to='rest.Dog')),
                ('organiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myActivities', to='rest.owner')),
                ('participants', models.ManyToManyField(related_name='activities', to='rest.Owner')),
            ],
        ),
    ]
