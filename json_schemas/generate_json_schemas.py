"""
This script is run in the tox 'json_schemas' environment.
It creates json schema files as described in the README.md in the same directory.
"""

import importlib
import inspect
import json
import pathlib
import pkgutil

pkgs = ["bo", "com"]
for pkg in pkgs:
    modls = [
        name for _, name, _ in pkgutil.iter_modules([str(pathlib.Path(__file__).parent.parent / "src" / "bo4e" / pkg)])
    ]
    for x in modls:
        modl_name = f"bo4e.{pkg}.{x}"
        modl = importlib.import_module(modl_name)
        # pylint: disable=cell-var-from-loop
        cls_list = inspect.getmembers(modl, lambda member: inspect.isclass(member) and member.__module__ == modl_name)
        for name, cls in cls_list:
            this_directory = pathlib.Path(__file__).parent.absolute()
            file_path = this_directory / pkg / (name + ".json")  # pylint:disable=invalid-name
            schema_json_dict = json.loads(cls.schema_json(ensure_ascii=False, sort_keys=True, indent=4))
            if "definitions" in schema_json_dict:
                for definition in schema_json_dict["definitions"].values():
                    # this sanitizing step is necessary since python 3.11
                    definition["description"] = definition["description"].strip()
            with open(file_path, "w+", encoding="utf-8") as json_schema_file:
                json_schema_file.write(json.dumps(schema_json_dict, indent=4))
