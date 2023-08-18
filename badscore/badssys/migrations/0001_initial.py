# Generated by Django 3.2.20 on 2023-08-16 19:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CorporateCrops',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'CorporateCrops',
            },
        ),
        migrations.CreateModel(
            name='CorporateSociety',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('region', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CorporateSociety',
            },
        ),
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('priceperkg', models.DecimalField(decimal_places=1, max_digits=10)),
                ('moisturePercentage', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
            options={
                'db_table': 'Crops',
            },
        ),
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('corporate_society', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badssys.corporatesociety')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Farmer',
            },
        ),
        migrations.CreateModel(
            name='CropSales',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('quantityInKg', models.DecimalField(decimal_places=1, max_digits=10)),
                ('totalPay', models.DecimalField(decimal_places=1, max_digits=17)),
                ('cropSold', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badssys.corporatecrops')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badssys.farmers')),
            ],
            options={
                'db_table': 'CropSales',
            },
        ),
        migrations.AddField(
            model_name='corporatecrops',
            name='corporate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badssys.corporatesociety'),
        ),
        migrations.AddField(
            model_name='corporatecrops',
            name='crop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badssys.crops'),
        ),
    ]
