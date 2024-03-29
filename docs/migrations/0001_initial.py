# Generated by Django 4.1.1 on 2022-09-15 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('url', models.CharField(blank=True, max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('parentId', models.CharField(blank=True, max_length=64)),
                ('type', models.CharField(choices=[('FILE', 'File'), ('FOLDER', 'Folder')], max_length=64)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'SystemItem',
            },
        ),
    ]
