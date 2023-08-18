from django import forms
from graphene_django.forms.mutation import DjangoModelFormMutation
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from django.forms.widgets import TextInput
from django.core import validators
from django.forms import ModelForm
from usermanagement.models import User


class LongCharField(forms.Field):
    def __init__(
        self, max_length=10**10, min_length=None, strip=True, empty_value='',
        **kwargs
    ):
        self.max_length = max_length  # Satisfy management validation.
        self.min_length = min_length
        self.strip = strip
        self.empty_value = empty_value
        super().__init__(**kwargs)

        if min_length is not None:
            self.validators.append(
                validators.MinLengthValidator(int(min_length))
            )
        if max_length is not None:
            self.validators.append(
                validators.MaxLengthValidator(int(max_length))
            )


class CorporateSocietyForm(ModelForm):
    name = forms.CharField(max_length=100, required=False)
    region = forms.CharField(max_length=64, required=False)
    district = forms.CharField(max_length=64, required=False)
    admin = forms.CharField(required=False)

    def clean_admin(self):
        admin = self.cleaned_data['admin']
        try:
            User.objects.get(admin=admin)
        except ObjectDoesNotExist as e:
            raise forms.ValidationError(e)
        return admin

    class Meta:
        model = CorporateSociety
        fields = "__all__"

