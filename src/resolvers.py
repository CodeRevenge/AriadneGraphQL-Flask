from ariadne import ObjectType, QueryType
import json

query = QueryType()
planet = ObjectType("Planet")
planet_types = ObjectType("PlanetType")


@query.field("planets")
def _planets(*_):
    with open('./data/planets.json') as file:
        data = json.load(file)
        planets = [
            planet for resident in data if True
        ]
        return data

@query.field("planetTypes")
def _planet_types(*_):
    with open('./data/planetTypes.json') as file:
        data = json.load(file)
        return data

@query.field("planet")
def _planet_id(*_, _id):
    with open('./data/planets.json') as file:
        data = json.load(file)
        return [planet for planet in data if planet["_id"] == int(_id)][0]

@planet.field("planetType")
def _planet_types_id(planet,info):
    with open('./data/planetTypes.json') as file:
        data = json.load(file)

        return [types for types in data if types["_id"] in planet["typeId"]]

resolvers = [planet, planet_types, query]