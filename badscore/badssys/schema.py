import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from .models import *
from usermanagement.models import User


class CorporateSocietyTypes(DjangoObjectType):
    class Meta:
        model = CorporateSociety
        fields = "__all__"
        interface = (relay.Node,)


class FarmersTypes(DjangoObjectType):
    class Meta:
        model = Farmers
        fields = "__all__"
        interface = (relay.Node,)


class CropsTypes(DjangoObjectType):
    class Meta:
        model = Crops
        fields = "__all__"
        interface = (relay.Node,)


class CorporateCropsTypes(DjangoObjectType):
    class Meta:
        model = CorporateCrops
        fields = "__all__"
        interface = (relay.Node,)


class CropSalesTypes(DjangoObjectType):
    class Meta:
        model = CropSales
        fields = "__all__"
        interface = (relay.Node,)


class Query:
    corporate_societies = graphene.List(CorporateSocietyTypes)
    farmers = graphene.List(FarmersTypes)
    crops = graphene.List(CropsTypes)
    corporate_crops = graphene.List(CorporateCropsTypes,
                                    corporate=graphene.String(required=False)
                                    )
    farmer_crop_sale = graphene.List(
        CropSalesTypes, farmer=graphene.String(required=False)
    )
    crop_sales_list = graphene.List(CropSalesTypes)
    me_farmer = graphene.List(FarmersTypes, farmer=graphene.String(required=False))
    def resolve_corporate_societies(self, info):
        return CorporateSociety.objects.all()

    def resolve_farmers(self, info):
        return Farmers.objects.all()

    def resolve_crops(self, info):
        return Crops.objects.all()

    def resolve_corporate_crops(self, info, corporate):
        return CorporateCrops.objects.filter(corporate=corporate)

    def resolve_farmer_crop_sale(self, info, farmer):
        # Get the user by email
        user = User.objects.get(email=farmer)

        # Get crop sales for the farmer
        farmer_crop_sales = CropSales.objects.filter(farmer__farmer=user)

        return farmer_crop_sales
        # user = User.objects.get(email=farmer)
        # print(user)
        # farmer_crop_sales = []
        # sales_farmer = Farmers.objects.filter(farmer=user)
        # x = [ x for x in sales_farmer]
        # for farmerdata in x:
        #     farmer_crop_sales.append(CropSales.objects.filter(farmer=farmerdata))
        # return farmer_crop_sales

    def resolve_me_farmer(self, info, farmer):
        user = User.objects.get(email=farmer)
        return Farmers.objects.filter(farmer=user)

    def resolve_crop_sales_list(self, info):
        return CropSales.objects.all()
