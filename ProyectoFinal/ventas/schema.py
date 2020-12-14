import graphene
import CarpetaProductos.schema

class Query(CarpetaProductos.schema.Query, graphene.ObjectType):
    pass

class Mutation(CarpetaProductos.schema.Mutation, graphene.ObjectType):
    pass

schema =graphene.Schema(query=Query, mutation=Mutation)
