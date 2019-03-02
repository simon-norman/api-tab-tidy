from .inactive_rec_schema import Mutation as InactiveRecMutations
from .tab_schema import Mutation as TabMutations
import graphene


class Mutations(InactiveRecMutations, TabMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutations)
