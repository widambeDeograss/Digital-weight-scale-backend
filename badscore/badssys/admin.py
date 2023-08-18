from django.contrib import admin
from .models import *
from django.apps import apps

# Register your models here.
admin.site.register(CropSales)
admin.site.register(Crops)
admin.site.register(Farmers)
admin.site.register(CorporateCrops)
admin.site.register(CorporateSociety)
