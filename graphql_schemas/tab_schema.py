import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.models import Tab as TabModel
from models.models import db


class TabObject(SQLAlchemyObjectType):
    class Meta:
        model = TabModel
        interfaces = (graphene.relay.Node,)


class CreateTab(graphene.Mutation):
    class Arguments:
        tab_id = graphene.Int(required=True)
        created_timestamp = graphene.DateTime(required=True)


    tab = graphene.Field(lambda: TabObject)

    def mutate(self, info, tab_id, created_timestamp):
        tab = TabModel(tab_id=tab_id, created_timestamp=created_timestamp, last_active_timestamp=created_timestamp)
        db.session.add(tab)
        db.session.commit()
        return CreateTab(tab=tab)

class UpdateTab(graphene.Mutation):
    class Arguments:
        tab_id = graphene.Int(required=True)
        last_active_timestamp = graphene.DateTime()
        closed_timestamp = graphene.DateTime()


    tab = graphene.Field(lambda: TabObject)

    def mutate(self, info, tab_id, **kwargs):
        tab = TabModel.query.get(tab_id)
        tab.closed_timestamp = kwargs.get('closed_timestamp', None)
        tab.last_active_timestamp = kwargs.get('last_active_timestamp', None)
        db.session.commit()
        return UpdateTab(tab=tab)


class Mutation(graphene.ObjectType):
    create_tab = CreateTab.Field()
    update_tab = UpdateTab.Field()


schema = graphene.Schema(mutation=Mutation)
