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
                            "id": dat['farmer']['id']
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
    pass

