mport graphene
import django_filters
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay.node.node import from_global_id
from .models import empleado,categoria, producto, factura
class empleadoNode (DjangoObjectType):
    class Meta:
        model = empleado
        filter_fields = ['usuarios','Contrasenia','Roles']
        interfaces = (graphene.relay.Node,)
class categoriaNode (DjangoObjectType):
    class Meta:
        model = categoria
        filter_fields=['nombre_categoria']
        interfaces = (graphene.relay.Node,)
