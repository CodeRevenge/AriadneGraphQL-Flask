from ariadne import QueryType, graphql_sync, fallback_resolvers
from ariadne.contrib.federation import make_federated_schema
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from .typedefs import type_defs
from .resolvers import resolvers

schema = make_federated_schema(type_defs, resolvers)
