# Generated by Django 5.1.1 on 2024-09-04 07:41

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('description', models.TextField(default='Default')),
                ('stocks', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('recom_status_last_update', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]