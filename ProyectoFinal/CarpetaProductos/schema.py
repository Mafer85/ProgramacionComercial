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

class productoNode(DjangoObjectType):
    class Meta:
        model = producto
        filter_fields =['nombre_producto','Descripcion','Existencia','Precio','Categoria']
        interfaces = (graphene.relay.Node,)

class facturaNode(DjangoObjectType):
    class Meta:
        model = factura
        filter_fields=['Nombre_Cliente','Producto','serie','nit','cantidad','Fecha','total']
        interfaces = (graphene.relay.Node,)

class createEmpleado(graphene.relay.ClientIDMutation):
    Empleado = graphene.Field(empleadoNode)

    class Input:
        usuarios=  graphene.String()
        Contrasenia = graphene.String()
        Roles = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Empleado = empleado(
        usuarios = input.get('usuarios'),
        Contrasenia = input.get('Contrasenia'),
        Roles = input.get('Roles')
        )
        Empleado.save()
        return createEmpleado(Empleado = Empleado)


class UpdateEmpleado(graphene.relay.ClientIDMutation):
    Empleado = graphene.Field(empleadoNode)

    class Input:
        id = graphene.String()
        usuarios = graphene.String()
        Contrasenia = graphene.String()
        Roles = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Empleado = empleado.objects.get(
            pk =from_global_id(input.get('id'))[1])
        Empleado.usuarios = input.get('usuarios')
        Empleado.Contrasenia = input.get('Contrasenia')
        Empleado.Roles = input.get('Roles')
        Empleado.save()
        return UpdateEmpleado(Empleado=Empleado)

class DeleteEmpleado(graphene.relay.ClientIDMutation):
    Empleado = graphene.Field(empleadoNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root,info, **input):
        Empleado = empleado.objects.get(
            pk=from_global_id(input.get('id'))[1]
        )
        Empleado.delete()
        return DeleteEmpleado(Empleado = Empleado)


class CreateProducto(graphene.relay.ClientIDMutation):
    Producto = graphene.Field(productoNode)

    class Input:
        nombre_producto = graphene.String()
        Descripcion = graphene.String()
        Existencia = graphene.Int()
        Precio = graphene.Float()
        nombre_categoria= graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Producto = producto(
        nombre_producto = input.get('nombre_producto'),
        Descripcion = input.get('Descripcion'),
        Existencia = input.get('Existencia'),
        Precio = input.get('Precio'),
        Categoria = categoria.objects.get(
            nombre_categoria = input.get('nombre_categoria')
        )
        )
        Producto.save()
        return CreateProducto(Producto = Producto)

class UpdateProducto(graphene.relay.ClientIDMutation):
    Producto = graphene.Field(productoNode)

    class Input:
        id = graphene.String()
        nombre_producto = graphene.String()
        Descripcion = graphene.String()
        Existencia = graphene.Int()
        Precio = graphene.Float()
        nombre_categoria= graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Producto = producto.objects.get(
            pk = from_global_id(input.get('id'))[1])
        Producto.nombre_producto = input.get('nombre_producto')
        Producto.Descripcion = input.get('Descripcion')
        Producto.Existencia = input.get('Existencia')
        Producto.Precio = input.get('Precio')
        Producto.Categoria = categoria.objects.get(
            nombre_categoria = input.get('nombre_categoria')
        )
        Producto.save()
        return UpdateProducto(Producto=Producto)

class DeleteProducto(graphene.relay.ClientIDMutation):
    Producto = graphene.Field(productoNode)

    class Input:
        id = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        Producto = producto.objects.get(
            pk = from_global_id(input.get('id'))[1])
        Producto.delete()
        return DeleteProducto(Producto=Producto)



class Query(object):
    empleado = graphene.relay.Node.Field(empleadoNode)
    all_empleados = DjangoFilterConnectionField(empleadoNode)

    categoria = graphene.relay.Node.Field(categoriaNode)
    all_categorias = DjangoFilterConnectionField(categoriaNode)

    producto = graphene.relay.Node.Field(productoNode)
    all_productos = DjangoFilterConnectionField(productoNode)

    factura = graphene.relay.Node.Field(facturaNode)
    all_facturas = DjangoFilterConnectionField(facturaNode)
