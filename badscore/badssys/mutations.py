import graphene
from datetime import datetime
import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers.json import DjangoJSONEncoder
from .models import *
from .schema import *
from usermanagement.models import User


class CorporateSocietyMutation(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        admin = graphene.String(required=True)
        region = graphene.String()
        district = graphene.String()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    corporate_society = graphene.Field(lambda: CorporateSocietyTypes)

    @classmethod
    def mutate(clx, root, info, **args):
        name = args.get('name')
        admin = args.get('admin')
        region = args.get('region')
        district = args.get('district')
        success = False
        errors = []

        print(admin)

        try:
            cop_admin = User.objects.get(email=admin)
            cop_admin.role = 2
            cop_admin.save()
            print(cop_admin)
            corporate_society = CorporateSociety(name=name, admin=cop_admin, region=region, district=district)
            corporate_society.save()
            success = True
        except Exception as e:
            errors.append(e)
        return CorporateSocietyMutation(errors=errors, success=success)


class FarmersMutation(graphene.Mutation):

    class Arguments:
        farmerPhone = graphene.String()
        society = graphene.String()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    farmers = graphene.Field(lambda: FarmersTypes)

    @classmethod
    def mutate(clx, root, info, **args):
        farmerphone = args.get('farmerPhone')
        society = args.get('society')
        success = False
        errors = []

        try:
            cop_farmer = User.objects.get(phone_number=farmerphone)
            societ = CorporateSociety.objects.get(name=society)

            farmer = Farmers(farmer=cop_farmer, corporate_society=societ)
            farmer.save()
            success = True
        except Exception as e:
            errors.append(e)
        return CorporateSocietyMutation(errors=errors, success=success)


class CropsMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        priceperkg = graphene.Float()
        moisturePercentage = graphene.Float()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    crops = graphene.Field(lambda: CropsTypes)

    @classmethod
    def mutate(clx, root, info, **args):
        name = args.get('name')
        priceperkg = args.get('priceperkg')
        moisturePercentage = args.get('moisturePercentage')
        success = False
        errors = []

        try:

            crop = Crops(name=name, priceperkg=priceperkg, moisturePercentage=moisturePercentage)
            crop.save()
            success = True
        except Exception as e:
            errors.append(e)
        return CorporateSocietyMutation(errors=errors, success=success)


class CorporateCropsMutation(graphene.Mutation):

    class Arguments:
        crop = graphene.String()
        corporate = graphene.String()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    corporate_crops = graphene.Field(lambda: CorporateCropsTypes)

    @classmethod
    def mutate(clx, root, info, **args):
        crop = args.get('crop')
        corporate = args.get('corporate')
        success = False
        errors = []

        try:
            crop = Crops.objects.get(id=crop)
            societ = CorporateSociety.objects.get(name=corporate)

            corporate_crops = CorporateCrops(crop=crop, corporate=societ)
            corporate_crops.save()
            success = True
        except Exception as e:
            errors.append(e)
        return CorporateSocietyMutation(errors=errors, success=success)


class CropSalesMutation(graphene.Mutation):
    class Arguments:
        cropSold = graphene.String()
        farmer = graphene.String()
        quantity_in_kg = graphene.Float()
        total_pay = graphene.Float()

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)
    crops_sale = graphene.Field(lambda: CropSalesTypes)

    @classmethod
    def mutate(clx, root, info, **args):
        crop = args.get('cropSold')
        farmer = args.get('farmer')
        quantity_in_kg = args.get('quantity_in_kg')
        total_pay = args.get('total_pay')
        success = False
        errors = []

        try:
            farmer = Farmers.objects.get(id=farmer)
            cor_crop = CorporateCrops.objects.get(id=crop)

            #CROP SALES CALCULATIONS GOES HERE

            crops_sale = CropSales(farmer=farmer, cropSold=cor_crop, quantityInKg=quantity_in_kg, totalPay=total_pay )
            crops_sale.save()
            success = True
        except Exception as e:
            errors.append(e)
        return clx(
            errors=errors, success=success
        )

