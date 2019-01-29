import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models.tab_recording import TabRecording as TabRecordingModel
from models.tab_recording import db


class TabRecordingObject(SQLAlchemyObjectType):
    class Meta:
        model = TabRecordingModel
        interfaces = (graphene.relay.Node,)


class CreateTabRecording(graphene.Mutation):
    class Arguments:
        tabid = graphene.String(required=True)
        status = graphene.String(required=True)

    tab_recording = graphene.Field(lambda: TabRecordingObject)

    def mutate(self, info, tabid, status):

        tab_recording = TabRecordingModel(tabid=tabid, status=status)

        db.session.add(tab_recording)
        db.session.commit()
        return CreateTabRecording(tab_recording=tab_recording)


class Mutation(graphene.ObjectType):
    create_tab_recording = CreateTabRecording.Field()


schema = graphene.Schema(mutation=Mutation)
