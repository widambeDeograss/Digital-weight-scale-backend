import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required
from .models import *


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
    get_farmer_crop_sale = graphene.Field(
        CropSalesTypes, farmer=graphene.String(required=False)
    )
    crop_sales_list = graphene.List(CropSalesTypes)

    def resolve_corporate_societies(self, info):
        return CorporateSociety.objects.all()

    def resolve_farmers(self, info):
        return Farmers.objects.all()

    def resolve_crops(self, info):
        return Crops.objects.all()

    def resolve_corporate_crops(self, info, corporate):
        return CorporateCrops.objects.filter(corporate= corporate)

    def resolve_get_farmer_crop_sale(self, info, farmer):
        return CropSales.objects.filter(farmer=farmer)

    def resolve_crop_sales_list(self, info):
        return CropSales.objects.all()
