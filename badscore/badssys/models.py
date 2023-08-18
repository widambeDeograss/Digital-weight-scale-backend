from django.db import models
from datetime import datetime
from decimal import Decimal
from usermanagement.models import User
import uuid


class CorporateSociety(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    region = models.CharField(max_length=20)
    district = models.CharField(max_length=20)

    REQUIRED_FIELDS = ['name', 'admin', 'region', 'district']

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CorporateSociety'


class Farmers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    corporate_society = models.ForeignKey(CorporateSociety, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['farmer', 'corporate_society']

    def __str__(self):
        return self.farmer

    class Meta:
        db_table = 'Farmer'


class Crops(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    priceperkg = models.DecimalField(max_digits=10, decimal_places=1)
    moisturePercentage = models.DecimalField(max_digits=2, decimal_places=2)

    REQUIRED_FIELDS = ['name', 'priceperkg', 'moisturePercentage']

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Crops'


class CorporateCrops(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    crop = models.ForeignKey(Crops, on_delete=models.CASCADE)
    corporate = models.ForeignKey(CorporateSociety, on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['crop', 'corporate']

    def __str__(self):
        return self.crop.name

    class Meta:
        db_table = 'CorporateCrops'


class CropSales(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cropSold = models.ForeignKey(CorporateCrops, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmers, on_delete=models.CASCADE)
    quantityInKg = models.DecimalField(max_digits=10, decimal_places=1)
    totalPay = models.DecimalField(max_digits=17, decimal_places=1)

    REQUIRED_FIELDS = ['cropSold', 'quantityInKg', 'totalPay']

    def __str__(self):
        return self.cropSold

    class Meta:
        db_table = 'CropSales'

