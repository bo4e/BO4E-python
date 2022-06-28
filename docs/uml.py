import importlib
import inspect
import os
import pkgutil
import re
from re import Pattern

import networkx as nx  # type: ignore[import]
from pydantic.fields import (
    MAPPING_LIKE_SHAPES,
    SHAPE_TUPLE,
    SHAPE_GENERIC,
    SHAPE_SINGLETON,
    SHAPE_NAME_LOOKUP,
    ModelField,
)
from pydantic.typing import display_as_type


def build_dots(module_dir: str, output_dir: str, radius: int = 1) -> None:
    pkgs_scope = {
        "bo": ["bo", "com"],
        "com": ["bo", "com"],
    }
    regex_incl_network = re.compile(r"^bo4e\.(" + "|".join(set(sum(pkgs_scope.values(), []))) + r")")
    regex_excl_network = re.compile(r"^.*Constrained")
    uml_network = nx.MultiDiGraph()
    parse_to_dot = []
    for pkg in pkgs_scope.keys():
        modls = [name for _, name, _ in pkgutil.iter_modules([module_dir + os.path.sep + pkg])]
        for x in modls:
            modl_name = f"bo4e.{pkg}.{x}"
            modl = importlib.import_module(modl_name)
            cls_list = inspect.getmembers(
                modl, lambda member: inspect.isclass(member) and member.__module__ == modl_name
            )
            for name, cls in cls_list:
                modl_namespace = f"{cls.__module__}.{name}"
                parse_to_dot.append(modl_namespace)
                if not uml_network.has_node(modl_namespace):
                    recursive_helper(cls, modl_namespace, uml_network, regex_incl_network, regex_excl_network)

    print("Successfully created relationship network.")

    for modl_to_parse in parse_to_dot:
        spl = modl_to_parse.split(".")
        modl_cls_name = spl[-1]
        dot_path = output_dir + f"{os.path.sep}dots{os.path.sep}" + os.path.sep.join(spl[0:-2])
        dot_file = f"{modl_cls_name}.dot"
        uml_subgraph = nx.ego_graph(uml_network, modl_to_parse, radius=radius, undirected=False)
        dot_content = 'digraph "' + modl_cls_name + '" {\nrankdir=BT\ncharset="utf-8"\n'
        for node in uml_subgraph.nodes:
            dot_content += uml_subgraph.nodes[node]["dot_node_str"] + "\n"
        for edge in uml_subgraph.edges:
            dot_content += uml_subgraph.edges[edge]["dot_edge_str"] + "\n"
        dot_content += "}\n"

        os.makedirs(dot_path, exist_ok=True)
        with open(f"{dot_path}{os.path.sep}{dot_file}", "w") as f:
            f.write(dot_content)
            # print(f'"{dot_path}{os.path.sep}{dot_file}" created.')
    print("Successfully created dot files.")


def recursive_helper(  # type: ignore[no-untyped-def]
    cls_cur,
    modl_namespace: str,
    uml_network: nx.MultiDiGraph,
    regex_incl_network: Pattern[str],
    regex_excl_network: Pattern[str],
) -> None:
    # print(f'"{modl_namespace}" added.')
    uml_network.add_node(modl_namespace, model_cls=cls_cur, dot_node_str="will be replaced")
    dot_cls_str = rf'"{modl_namespace}" [color="black", fontcolor="black", label="' + "{" + rf"{modl_namespace}|"
    for model_field in cls_cur.__fields__.values():
        dot_cls_str += f"{model_field.alias} : {model_field_str(model_field)}"
        if not model_field.required:
            dot_cls_str += f" = {model_field.default}"
        dot_cls_str += r"\l"

        type_modl_namespace = f"{model_field.type_.__module__}.{model_field.type_.__name__}"
        if re.match(regex_incl_network, type_modl_namespace) and not re.match(regex_excl_network, type_modl_namespace):
            if not uml_network.has_node(type_modl_namespace):
                recursive_helper(
                    model_field.type_, type_modl_namespace, uml_network, regex_incl_network, regex_excl_network
                )
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
                recursive_helper(parent, type_modl_namespace, uml_network, regex_incl_network, regex_excl_network)
            uml_network.add_edge(
                modl_namespace,
                type_modl_namespace,
                dot_edge_str=f'"{modl_namespace}" -> "{type_modl_namespace}" [arrowhead="empty", arrowtail="none"];',
            )


def model_field_str(model_field: ModelField) -> str:
    # Copied from pydantic.field.ModelField._type_display()
    t = display_as_type(model_field.type_)

    # have to do this since display_as_type(self.outer_type_) is different (and wrong) on python 3.6
    if model_field.shape in MAPPING_LIKE_SHAPES:
        t = f"Mapping[{display_as_type(self.key_field.type_)}, {t}]"  # type: ignore
    elif model_field.shape == SHAPE_TUPLE:
        t = "Tuple[{}]".format(", ".join(display_as_type(f.type_) for f in self.sub_fields))  # type: ignore
    elif model_field.shape == SHAPE_GENERIC:
        assert model_field.sub_fields
        t = "{}[{}]".format(
            display_as_type(model_field.type_), ", ".join(display_as_type(f.type_) for f in model_field.sub_fields)
        )
    elif model_field.shape != SHAPE_SINGLETON:
        t = SHAPE_NAME_LOOKUP[model_field.shape].format(t)

    if model_field.allow_none and (model_field.shape != SHAPE_SINGLETON or not model_field.sub_fields):
        t = f"Optional[{t}]"
    return t
