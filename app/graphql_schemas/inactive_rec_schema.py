import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from app.models.inactive_rec import InactiveRec as InactiveRecModel
from app.extensions import db


class InactiveRec(SQLAlchemyObjectType):
    class Meta:
        model = InactiveRecModel
        interfaces = (graphene.relay.Node,)


class CreateInactiveRecInput(graphene.InputObjectType):
    tab_id = graphene.Int(required=True)
    inactive_timestamp = graphene.DateTime(required=True)
    active_timestamp = graphene.DateTime(required=True)


class CreateInactiveRec(graphene.Mutation):
    class Arguments:
        create_inactive_rec_input = CreateInactiveRecInput()

    inactive_rec = graphene.Field(lambda: InactiveRec)

    def mutate(self, info, create_inactive_rec_input):
        inactive_rec = InactiveRecModel(
            tab_id=create_inactive_rec_input.tab_id,
            active_timestamp=create_inactive_rec_input.active_timestamp,
            inactive_timestamp=create_inactive_rec_input.inactive_timestamp
        )

        db.session.add(inactive_rec)
        db.session.commit()
        return CreateInactiveRec(inactive_rec=inactive_rec)


class Mutation(graphene.ObjectType):
    create_inactive_rec = CreateInactiveRec.Field()
