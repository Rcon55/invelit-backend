from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_graphiql_handler
import graphene

from schemas import schema

app = FastAPI()

# app.add_route("/graphql", GraphQLApp(schema=schema))
# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema()))
app.mount("/graphql_app", GraphQLApp(schema, on_get=make_graphiql_handler()))  # Graphiql IDE
