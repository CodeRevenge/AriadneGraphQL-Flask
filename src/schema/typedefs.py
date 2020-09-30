from ariadne import load_schema_from_path
import pathlib


type_defs = load_schema_from_path(str(pathlib.Path(
    __file__).parent.absolute()) + '/schema.graphql')
