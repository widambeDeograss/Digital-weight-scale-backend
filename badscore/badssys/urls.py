from django.urls import path
from .views import *

urlpatterns = [
    path('farmer_info', FarmersView.as_view()),
    path("scale_crop_sale", CropSale.as_view())
]