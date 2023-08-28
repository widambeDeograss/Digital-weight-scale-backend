import graphene
from graphene import relay
from graphene_django.types import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import User


# class UserRole(graphene.Interface):
#     role = graphene.String()


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"
        interfaces = (relay.Node, )


class Query:
    users = graphene.List(UserType, role=graphene.String(required=False))
    corporate_admins = graphene.List(UserType, role=graphene.String(required=False))
    me = graphene.Field(UserType)

    @staticmethod
    def resolve_users(info, role):
        # if role != 'ALL':
        #     return User.objects.filter(role=role)
        return User.objects.all()

    @staticmethod
    def resolve_corporate_admins(info, role):
        return User.objects.filter(role=2)

    @login_required
    def resolve_me(self, info):
        return info.context.user
