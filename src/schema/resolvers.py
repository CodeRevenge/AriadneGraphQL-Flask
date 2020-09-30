from ariadne import ObjectType, QueryType
from ariadne.contrib.federation import FederatedObjectType
import json

query = QueryType()
planet = FederatedObjectType("Planet")
planet_types = FederatedObjectType("PlanetType")
stars = FederatedObjectType("Star")
galaxies = FederatedObjectType("Galaxy")


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


@query.field("stars")
def _stars(*_):
    with open('./data/stars.json') as file:
        data = json.load(file)
        return data


@query.field("galaxies")
def _galaxies(*_):
    with open('./data/galaxies.json') as file:
        data = json.load(file)
        return data


@query.field("planet")
def _planet_id(*_, _id):
    with open('./data/planets.json') as file:
        data = json.load(file)
        return [planet for planet in data if planet["_id"] == int(_id)][0]


@planet.field("planetType")
def _planet_types_id(parent, info):
    with open('./data/planetTypes.json') as file:
        data = json.load(file)
        return [types for types in data if types["_id"] in parent["typeId"]]


@planet.field("star")
def _star_planet(parent, _):
    with open('./data/stars.json') as file:
        data = json.load(file)
        return [star for star in data if star["_id"] == parent["star"]][0]


class Galaxy:
    @planet.field("galaxy")
    @stars.field("galaxy")
    def _galaxy_star(self, parent, _):
        with open('./data/galaxies.json') as file:
            data = json.load(file)
            return [galaxy for galaxy in data if galaxy["_id"] == parent["galaxy"]][0]


resolvers = [planet, planet_types, stars, galaxies, query]
