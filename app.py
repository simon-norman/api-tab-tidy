from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS

from models.tab import db
from graphql_schemas.tab_schema import schema


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)

    app = add_route(app)
    CORS(app)
    
    return app


def add_route(app):
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
