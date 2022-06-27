import importlib
import inspect
import os
import pkgutil
import re

import networkx as nx


def create_diagrams3(module_dir: str, output_dir: str, radius=1):
    pkgs_scope = {
        "bo": ["bo", "com"],
        "com": ["bo", "com"],
    }
    regex_incl_network = re.compile(r"^bo4e\.(" + "|".join(set(sum(pkgs_scope.values(), []))) + r")")
    regex_excl_network = re.compile(r"^.*Constrained")
    uml_network = nx.MultiDiGraph()
    parse_to_dot = []
    for pkg in pkgs_scope.keys():
        modls = [name for _, name, _ in pkgutil.iter_modules([module_dir + "\\" + pkg])]
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

    print("Successfully created relationship network.\n")

    for modl in parse_to_dot:
        spl = modl.split(".")
        modl_cls_name = spl[-1]
        dot_path = output_dir + "\\dots\\" + os.path.sep.join(spl[0:-2])
        dot_file = f"{modl_cls_name}.dot"
        uml_subgraph = nx.ego_graph(uml_network, modl, radius=radius, undirected=True)
        dot_content = 'digraph "' + modl_cls_name + '" {\nrankdir=BT\ncharset="utf-8"\n'
        for node in uml_subgraph.nodes:
            dot_content += uml_subgraph.nodes[node]["dot_node_str"] + "\n"
        for edge in uml_subgraph.edges:
            dot_content += uml_subgraph.edges[edge]["dot_edge_str"] + "\n"
        dot_content += "}\n"

        os.makedirs(dot_path, exist_ok=True)
        with open(rf"{dot_path}\{dot_file}", "w") as f:
            print(rf'"{dot_path}\{dot_file}" created.')
            f.write(dot_content)


def recursive_helper(cls_cur, modl_namespace, uml_network, regex_incl_network, regex_excl_network):
    print(f'"{modl_namespace}" added.')
    uml_network.add_node(modl_namespace, model_cls=cls_cur, dot_node_str="will be replaced")
    dot_cls_str = rf'"{modl_namespace}" [color="black", fontcolor="black", label="' + "{" + rf"{modl_namespace}|"
    for model_field in cls_cur.__fields__.values():
        dot_cls_str += f"{model_field.alias} : {model_field._type_display()}"
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
