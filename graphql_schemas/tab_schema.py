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


def calc_secs_since_tab_active(tab_id, current_timestamp):
    last_timestamp_active = TabModel.query.get(tab_id).last_timestamp_active
    time_since_tab_active = current_timestamp - last_timestamp_active
    return time_since_tab_active.seconds

class TabRecordingObject(SQLAlchemyObjectType):
    class Meta:
        model = TabRecordingModel
        interfaces = (graphene.relay.Node,)


class CreateTabRecording(graphene.Mutation):
    class Arguments:
        tab_id = graphene.Int(required=True)
        status = graphene.String(required=True)
        timestamp_recorded = graphene.DateTime(required=True)

    tab_recording = graphene.Field(lambda: TabRecordingObject)

    def mutate(self, info, tab_id, status, timestamp_recorded):
        if status == 'active':
            tab = TabModel.query.get(tab_id)
            tab.last_timestamp_active = timestamp_recorded
            db.session.commit()

        secs_since_active = calc_secs_since_tab_active(tab_id=tab_id, current_timestamp=timestamp_recorded)
        tab_recording = TabRecordingModel(tab_id=tab_id,
                                          status=status,
                                          secs_since_active=secs_since_active,
                                          timestamp_recorded=timestamp_recorded)
        db.session.add(tab_recording)
        db.session.commit()
        return CreateTabRecording(tab_recording=tab_recording)


class Mutation(graphene.ObjectType):
    create_tab_recording = CreateTabRecording.Field()
    create_tab = CreateTab.Field()


schema = graphene.Schema(mutation=Mutation)
