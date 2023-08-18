import graphene
import graphql_jwt
from usermanagement.mutations import (
    LoginMutation, RegisterMutation, SendConfirmationEmailMutation,
    ResetPasswordMutation, UserEditMutation
)
from badssys.mutations import (
    CorporateSocietyMutation, FarmersMutation, CropsMutation, CorporateCropsMutation, CropSalesMutation
)
from usermanagement.schema import Query as UsersQuery
from badssys.schema import Query as CropQuery


class Query(UsersQuery, CropQuery, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    register = RegisterMutation.Field()
    login = LoginMutation.Field()
    edit_user = UserEditMutation.Field()
    create_society = CorporateSocietyMutation.Field()
    add_farmer_to_society = FarmersMutation.Field()
    add_crops = CropsMutation.Field()
    add_corporate_crops = CorporateCropsMutation.Field()
    sale_crop = CropSalesMutation.Field()
    confirm_email = SendConfirmationEmailMutation.Field()
    reset_password = ResetPasswordMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

