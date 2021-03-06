from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from .extensions import db

from app.graphql_schemas.schema import schema


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)

    add_routes(app)
    CORS(app)

    return app


def add_routes(app):
    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
        )
    )

    return app


app = create_app()


if __name__ == '__main__':
    app.run()
