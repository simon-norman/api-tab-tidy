import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.models import TabRecording as TabRecordingModel, Tab as TabModel
from models.models import db


class TabObject(SQLAlchemyObjectType):
    class Meta:
        model = TabModel
        interfaces = (graphene.relay.Node,)


class CreateTab(graphene.Mutation):
    class Arguments:
        tab_id = graphene.Int(required=True)
        timestamp_created = graphene.DateTime(required=True)

    tab = graphene.Field(lambda: TabObject)

    def mutate(self, info, tab_id, timestamp_created):
        tab = TabModel(tab_id=tab_id, last_timestamp_active=timestamp_created)
        db.session.add(tab)
        db.session.commit()
        return CreateTab(tab=tab)


class TabRecordingObject(SQLAlchemyObjectType):
    class Meta:
        model = TabRecordingModel
        interfaces = (graphene.relay.Node,)


class CreateTabRecording(graphene.Mutation):
    class Arguments:
        tab_id = graphene.String(required=True)
        status = graphene.String(required=True)

    tab_recording = graphene.Field(lambda: TabRecordingObject)

    def mutate(self, info, tab_id, status, timestamp_recorded):
        tab_recording = TabRecordingModel(tab_id=tab_id, status=status)
        db.session.add(tab_recording)
        db.session.commit()
        return CreateTabRecording(tab_recording=tab_recording)


class Mutation(graphene.ObjectType):
    create_tab_recording = CreateTabRecording.Field()
    create_tab = CreateTab.Field()


schema = graphene.Schema(mutation=Mutation)
