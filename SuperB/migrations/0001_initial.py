# Generated by Django 3.2.7 on 2022-04-09 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('barcode', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveSmallIntegerField(help_text='<em>сом.</em>')),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id_student', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=60)),
                ('surname', models.CharField(max_length=60)),
                ('cash', models.PositiveIntegerField(help_text='<em>сом.</em>')),
            ],
        ),
    ]
