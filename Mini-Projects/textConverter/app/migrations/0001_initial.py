# Generated by Django 3.2.9 on 2022-06-26 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['csv'])])),
                ('email', models.EmailField(default=None, max_length=254)),
            ],
        ),
    ]
