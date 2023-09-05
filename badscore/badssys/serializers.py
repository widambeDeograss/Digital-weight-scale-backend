from django.contrib.auth import authenticate
from django.contrib.auth.hashers import *
from rest_framework import serializers
from .models import Farmers


class FarmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        fields = "__all__"
        depth = 3

