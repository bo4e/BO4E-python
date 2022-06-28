"""
Contains a method to build dot files from code. It is designed to work with pydantic and only tested in this project
so far.
"""
import importlib
import inspect
import os
import pkgutil
import re

import networkx as nx  # type: ignore[import]

# pylint: disable=no-name-in-module
from pydantic.fields import (
    MAPPING_LIKE_SHAPES,
    SHAPE_GENERIC,
    SHAPE_NAME_LOOKUP,
    SHAPE_SINGLETON,
    SHAPE_TUPLE,
    ModelField,
)
from pydantic.typing import display_as_type

pkgs_scope = {
    "bo": ["bo", "com"],
    "com": ["bo", "com"],
}
regex_incl_network = re.compile(r"^bo4e\.(" + "|".join(set(sum(pkgs_scope.values(), []))) + r")")
regex_excl_network = re.compile(r"^.*Constrained")


# pylint: disable=too-many-locals
def build_dots(module_dir: str, output_dir: str, radius: int = 1) -> None:
    """
    Build dot files for the packages `bo4e.bo` and `bo4e.com` for later use in sphinx with graphviz.
    For each class a seperate dot file (uml-diagram) will be generated. They include the class and its neighbors within
    a distance <= `radius`.
    """
    uml_network = nx.MultiDiGraph()
    parse_to_dot = []
    for pkg in pkgs_scope:
        modls = [name for _, name, _ in pkgutil.iter_modules([module_dir + os.path.sep + pkg])]
        for modl_name in modls:
            modl_namespace = f"bo4e.{pkg}.{modl_name}"
            modl = importlib.import_module(modl_namespace)
            # pylint: disable=cell-var-from-loop
            cls_list = inspect.getmembers(
                modl, lambda member: inspect.isclass(member) and member.__module__ == modl_namespace
            )
            for name, cls in cls_list:
                modl_namespace = f"{cls.__module__}.{name}"
                parse_to_dot.append(modl_namespace)
                if not uml_network.has_node(modl_namespace):
                    _recursive_add_class(cls, modl_namespace, uml_network)

    print("Successfully created relationship network.")

    for modl_to_parse in parse_to_dot:
        spl = modl_to_parse.split(".")
        modl_cls_name = spl[-1]
        dot_path = output_dir + f"{os.path.sep}dots{os.path.sep}" + os.path.sep.join(spl[0:-2])
        dot_file_name = f"{modl_cls_name}.dot"
        uml_subgraph = nx.ego_graph(uml_network, modl_to_parse, radius=radius, undirected=False)
        dot_content = 'digraph "' + modl_cls_name + '" {\nrankdir=BT\ncharset="utf-8"\n'
        for node in uml_subgraph.nodes:
            dot_content += uml_subgraph.nodes[node]["dot_node_str"] + "\n"
        for edge in uml_subgraph.edges:
            dot_content += uml_subgraph.edges[edge]["dot_edge_str"] + "\n"
        dot_content += "}\n"

        os.makedirs(dot_path, exist_ok=True)
        with open(f"{dot_path}{os.path.sep}{dot_file_name}", "w+", encoding="UTF-8") as dot_file:
            dot_file.write(dot_content)
            # print(f'"{dot_path}{os.path.sep}{dot_file}" created.')
    print("Successfully created dot files.")


def _recursive_add_class(  # type: ignore[no-untyped-def]
    cls_cur,
    modl_namespace: str,
    uml_network: nx.MultiDiGraph,
) -> None:
    """
    Add the specified class `cls_cur` to the `uml_network` and recursively add all classes found in fields and
    bases (super classes).
    """
    # print(f'"{modl_namespace}" added.')
    uml_network.add_node(modl_namespace, model_cls=cls_cur, dot_node_str="will be replaced")
    dot_cls_str = rf'"{modl_namespace}" [color="black", fontcolor="black", label="' + "{" + rf"{modl_namespace}|"
    for model_field in cls_cur.__fields__.values():
        dot_cls_str += f"{model_field.alias} : {_model_field_str(model_field)}"
        if not model_field.required:
            dot_cls_str += f" = {model_field.default}"
        dot_cls_str += r"\l"

        type_modl_namespace = f"{model_field.type_.__module__}.{model_field.type_.__name__}"
        if re.match(regex_incl_network, type_modl_namespace) and not re.match(regex_excl_network, type_modl_namespace):
            if not uml_network.has_node(type_modl_namespace):
                _recursive_add_class(model_field.type_, type_modl_namespace, uml_network)
            uml_network.add_edge(
                modl_namespace,
                type_modl_namespace,
                through_field=model_field,
                dot_edge_str=f'"{modl_namespace}" -> "{type_modl_namespace}" [arrowhead="diamond", arrowtail="none", fontcolor="green", label="{model_field.alias}", style="solid"];',
            )

    dot_cls_str += '|}", shape="record", style="solid"];'
    uml_network.nodes[modl_namespace]["dot_node_str"] = dot_cls_str
    for parent in cls_cur.__bases__:
        type_modl_namespace = f"{parent.__module__}.{parent.__name__}"
        if re.match(regex_incl_network, type_modl_namespace) and not re.match(regex_excl_network, type_modl_namespace):
            if not uml_network.has_node(type_modl_namespace):
                _recursive_add_class(parent, type_modl_namespace, uml_network)
            uml_network.add_edge(
                modl_namespace,
                type_modl_namespace,
                dot_edge_str=f'"{modl_namespace}" -> "{type_modl_namespace}" [arrowhead="empty", arrowtail="none"];',
            )


def _model_field_str(model_field: ModelField) -> str:
    """
    Parse the type of the ModelField to a printable string. Copied from pydantic.field.ModelField._type_display()
    """
    result_str = display_as_type(model_field.type_)

    # have to do this since display_as_type(self.outer_type_) is different (and wrong) on python 3.6
    if model_field.shape in MAPPING_LIKE_SHAPES:
        result_str = f"Mapping[{display_as_type(model_field.key_field.type_)}, {result_str}]"  # type: ignore
    elif model_field.shape == SHAPE_TUPLE:
        result_str = f"Tuple[{', '.join(display_as_type(sub_field.type_) for sub_field in model_field.sub_fields)}]"  # type: ignore
    elif model_field.shape == SHAPE_GENERIC:
        assert model_field.sub_fields
        result_str = f"{display_as_type(model_field.type_)}[{', '.join(display_as_type(sub_field.type_) for sub_field in model_field.sub_fields)}]"
    elif model_field.shape != SHAPE_SINGLETON:
        result_str = SHAPE_NAME_LOOKUP[model_field.shape].format(result_str)

    if model_field.allow_none and (model_field.shape != SHAPE_SINGLETON or not model_field.sub_fields):
        result_str = f"Optional[{result_str}]"
    return result_str
