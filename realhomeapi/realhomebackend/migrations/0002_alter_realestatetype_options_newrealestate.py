# Generated by Django 5.1.1 on 2024-10-27 18:17

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realhomebackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='realestatetype',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='NewRealEstate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=500)),
                ('bathrooms', models.IntegerField(default=0)),
                ('bedrooms', models.IntegerField(default=0)),
                ('minPrice', models.IntegerField(default=0)),
                ('maxPrice', models.IntegerField(default=0)),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realhomebackend.realestatetype')),
            ],
            options={
                'db_table': 'new_real_estates',
                'managed': True,
            },
        ),
    ]
