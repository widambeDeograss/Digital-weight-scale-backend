import decimal

# from BeemAfrica import Authorize
# from BeemAfrica.SMS import SMS
from .models import *
from rest_framework.views import *
from usermanagement.models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class FarmersView(APIView):
    permission_classes = [AllowAny]
    @staticmethod
    def post(request):
        farmer_phone = request.data
        print(farmer_phone)
        try:
            user = User.objects.get(phone_number=farmer_phone['phone'])
            user_data = User.objects.values('email', 'full_name').get(phone_number=farmer_phone['phone'])
            if user:
                print(user)
                farmer = Farmers.objects.filter(farmer=user)
                serializer = FarmersSerializer(data=farmer, many=True)
                # print(serializer)
                serializer.is_valid()
                farmer_data = []
                data = serializer.data
                for dat in data:
                    cop_soc = dat['corporate_society']['id']
                    cor_crops = CorporateCrops.objects.filter(corporate=cop_soc)
                    cor_crops_list = []
                    for ccl in cor_crops:
                        cor_crops_list.append(
                            {
                                "id": ccl.id,
                                "name": ccl.crop.name
                            }
                        )
                    data = {
                        "farmer": {
                            "id": dat['id']
                        },
                        "corporate": {
                            "id": dat['corporate_society']['id'],
                            "name": dat['corporate_society']['name']
                        },
                        "corporate_crops": cor_crops_list
                    }
                    farmer_data.append(data)
                mobile_farmer_data = {
                    "farmer": user_data,
                    "farmer_data":farmer_data
                }
                return Response(mobile_farmer_data)
        except User.DoesNotExist:
            return Response({'message': 'User Does Not Exist'})

#
# {
# "phone":"07756526"
# }


class CropSale(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        data = request.data
        crod_sell_id = data["cropId"]
        farmer_id = data["farmerId"]
        quantity_in_kg = data["quantity_in_kg"]
        farmer = Farmers.objects.get(id=farmer_id)
        cor_crop = CorporateCrops.objects.get(id=crod_sell_id)
        crop_price = cor_crop.crop.priceperkg
        crop_moisture = cor_crop.crop.moisturePercentage
        print(type(quantity_in_kg))
        print(type(crop_price))
        print(type(crop_moisture))

        #take moisture/ 100 multiply by the quantity in kg
        quantity_with_reduced_moisture = decimal.Decimal(str(quantity_in_kg)) - (decimal.Decimal(str(quantity_in_kg)) * (crop_moisture / 100))
        total_pay_price = quantity_with_reduced_moisture * crop_price
        crops_sale = CropSales.objects.create(farmer=farmer, cropSold=cor_crop, quantityInKg=quantity_in_kg, totalPay=total_pay_price)
        crops_sale.save()
        print(crops_sale.id)

        data_to_receipt = {
            "id": crops_sale.id,
            "cropSold": crops_sale.cropSold.crop.name,
            "farmer": crops_sale.farmer.farmer.full_name,
            "saledate": crops_sale.saledate,
            "quantity_before": quantity_in_kg,
            "moisturePercentage": crop_moisture,
            "quantityInKg": crops_sale.quantityInKg,
            "totalPay": total_pay_price
        }
        # message = (f'E-Mzani \n Ndugu {crops_sale.cropSold.crop.name} umeuza { crops_sale.cropSold.crop.name} \n '
        #            f'{quantity_in_kg}Kgs kwa {total_pay_price}Tsh Tarehe { crops_sale.saledate} \n '
        #            f'RECEIPT ID {crops_sale.id}')
        # Authorize('478040a68e5f755d',
        #           'ZTVkMzUwYWI5NjMwYjM2Zjc0ZTY1ZGQ5ZmQzZWNjNTMwYzRkOTEyYWRlODdhNWIxYmExYmQxOGZkMGNiODdiYg==')
        #
        # SMS.send_sms(message, crops_sale.farmer.farmer.phone)

        print(data_to_receipt)
        return Response(data_to_receipt)

# {
#     "cropId":"201c7c81-538d-49a4-85af-99325a74280f",
#     "farmerId":"e8d67685-c567-4e64-be3e-3a6a3eccd143",
#     "quantity_in_kg":123.3
# }
