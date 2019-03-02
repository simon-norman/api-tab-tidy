import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.tab import Tab as TabModel
from app.extensions import db


class Tab(SQLAlchemyObjectType):
    class Meta:
        model = TabModel
        interfaces = (graphene.relay.Node,)


class CreateTabInput(graphene.InputObjectType):
    tab_id = graphene.Int(required=True)
    created_timestamp = graphene.DateTime(required=True)


class CreateTab(graphene.Mutation):
    class Arguments:
        create_tab_input = CreateTabInput()

    tab = graphene.Field(lambda: Tab)

    def mutate(self, info, create_tab_input):
        tab = TabModel(
            tab_id=create_tab_input.tab_id,
            created_timestamp=create_tab_input.created_timestamp,
            last_active_timestamp=create_tab_input.created_timestamp
        )

        db.session.add(tab)
        db.session.commit()
        return CreateTab(tab=tab)


class UpdateTabInput(graphene.InputObjectType):
    tab_id = graphene.Int(required=True)
    closed_timestamp = graphene.DateTime()
    last_active_timestamp = graphene.DateTime()


class UpdateTab(graphene.Mutation):
    class Arguments:
        update_tab_input = UpdateTabInput()

    tab = graphene.Field(lambda: Tab)

    def mutate(self, info, update_tab_input):
        tab = TabModel.query.get(update_tab_input.tab_id)
        tab.closed_timestamp = update_tab_input.closed_timestamp
        tab.last_active_timestamp = update_tab_input.last_active_timestamp
        db.session.commit()
        return UpdateTab(tab=tab)


class Mutation(graphene.ObjectType):
    create_tab = CreateTab.Field()
    update_tab = UpdateTab.Field()
