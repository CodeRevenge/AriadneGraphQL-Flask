from ariadne import QueryType, graphql_sync, make_executable_schema, fallback_resolvers
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
from typedefs import type_defs
from resolvers import resolvers



schema = make_executable_schema(type_defs, resolvers)