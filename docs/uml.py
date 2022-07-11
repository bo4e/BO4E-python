"""
Contains functionality to build UML files from code. Eventually additional parsing into svg as for now for the Plantuml
parser. Currently, this the only supported parser.
It is designed to work together with `pydantic` and only is tested in this project so far.
"""
import importlib
import inspect
import os
import pkgutil
import re
import requests
import shlex
import subprocess
from abc import ABCMeta, abstractmethod
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Type, cast

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
from pydantic.main import ModelMetaclass
from pydantic.typing import display_as_type

pkgs = {
    "bo": {
        "scope": ["bo", "com"],
        "color": "#B6D7A8",
    },
    "com": {
        "scope": ["bo", "com"],
        "color": "#e0a86c",
    },
}
"""
UML-files will be created only for classes in the packages indicated by the keys of this dict. Additionally for every
package one can define a scope meaning that for every class in e.g. `bo` the UML-file will contain only classes in
packages defined by the value of the dict-entry.
This is for example useful if you want to include bo4e.enum classes in the UMLs but dont want to create UML-files for
them.
"""

pkgs_all = set(sum([pkg["scope"] for pkg in pkgs.values()], []))  # type:ignore[type-var]
"""
Contains all packages possibly included inside the network. They are determined by all scopes in `pkgs`.
"""

# accent_color = "#6AA84F"
regex_incl_network = re.compile(r"^bo4e\.(" + "|".join(pkgs_all) + r")")
"""
Regex to include all classes with namespaces matching this pattern. Note that this pattern has to start with `^`.
(because `re.match()` is called) Currently, this pattern matches all classes which appear in the values of `pkgs-scope`
"""

regex_excl_network = re.compile(r"^.*Constrained")
"""
Regex to explicitly exclude all classes with namespaces matching this pattern. Note that this pattern has to start with
`^`. (because `re.match()` is called) Currently, this pattern matches all classes containing `Constrained`.
This is necessary because e.g. ConstrainedStr is a inner class of `BaseModel` (I think - it is from pydantic :))
being inherited by all classes in this project. Therefore, their namespace starts with the respective class e.g.
`bo4e.bo.angebot.Angebot.ConstrainedStr`.
"""

#: Define shorthand for Cardinality type since none of the values have to be provided.
Cardinality = Optional[Tuple[Optional[str], Optional[str]]]

#: Define the link base domain used in svg links
LINK_DOMAIN = "https://bo4e-python.readthedocs.io/en/latest"

# link domain to test links only local.
# LINK_DOMAIN = f"file:///{Path.cwd().parent}/.tox/docs/tmp/html"


class _UMLNetworkABC(nx.MultiDiGraph, metaclass=ABCMeta):
    """
    Defines the abstract base class for all UML-Parsers. Currently, there is only a Plantuml-parser, but you can easily
    add a parser by implementing all abstract methods in a subclass.
    """

    def add_class(self, node: str, cls: ModelMetaclass) -> None:
        """
        Adds a class to the UML-Network. It copies the __fields__ dictionary because it will possibly be mutated when
        adding superclasses to the network.
        """
        super().add_node(node, cls=cls, fields=cls.__fields__.copy())  # type:ignore[attr-defined]

    def add_extension(self, node1: str, node2: str) -> None:
        """
        Adds an extension-relation: node1 ---|> node2. All fields of the superclass will be removed in node1 to improve
        clarity.
        """
        super().add_edge(node1, node2, type="extension")
        list(map(self.nodes[node1]["fields"].__delitem__, self.nodes[node2]["cls"].__fields__.keys()))

    # pylint: disable=too-many-arguments
    def add_association(
        self, node1: str, node2: str, through_field: ModelField, card1: Cardinality = None, card2: Cardinality = None
    ) -> None:
        """
        Adds an association-relation. `node1` references `node2` in its field `through_field`. Additionally, you can
        provide information relating to the cardinality of the association.
        """
        super().add_edge(node1, node2, type="association", through_field=through_field, card1=card1, card2=card2)

    def get_node_str(self, node: str, detailed: bool = True, rebuild: bool = True, root_node: str = None) -> str:
        """
        Gets the string representation of the node `node`. If `rebuild` is `false` and this string was already built
        before, the string will be loaded from cache. If you provide a `root_node` this feature is not recommended.
        """
        if detailed:
            if "node_str_detailed" not in self.nodes[node] or rebuild:
                self.nodes[node]["node_str_detailed"] = self._node_to_str(node, detailed, root_node)
            return self.nodes[node]["node_str_detailed"]

        if "node_str" not in self.nodes[node] or rebuild:
            self.nodes[node]["node_str"] = self._node_to_str(node, detailed, root_node)
        return self.nodes[node]["node_str"]

    # pylint: disable=too-many-arguments
    def get_edge_str(
        self, node1: str, node2: str, index: int, detailed: bool = True, rebuild: bool = True, root_node: str = None
    ) -> str:
        """
        Gets the string representation of the edge. If `rebuild` is `false` and this string was already built
        before, the string will be loaded from cache. If you provide a `root_node` this feature is not recommended.
        """
        if detailed:
            if "edge_str_detailed" not in self[node1][node2][index] or rebuild:
                self[node1][node2][index]["edge_str_detailed"] = self._edge_to_str(
                    node1, node2, index, detailed, root_node
                )
            return self[node1][node2][index]["edge_str_detailed"]

        if "edge_str" not in self[node1][node2][index] or rebuild:
            self[node1][node2][index]["edge_str"] = self._edge_to_str(node1, node2, index, detailed, root_node)
        return self[node1][node2][index]["edge_str"]

    @abstractmethod
    def _node_to_str(self, node: str, detailed: bool, root_node: Optional[str]) -> str:
        """
        Returns a string representation of the provided `node` with a possibly provided `root_node`.
        """
        raise NotImplementedError("This method should be overridden.")

    # pylint: disable=too-many-arguments
    @abstractmethod
    def _edge_to_str(self, node1: str, node2: str, index: int, detailed: bool, root_node: Optional[str]) -> str:
        """
        Returns a string representation of the provided edge with a possibly provided `root_node`.
        """
        raise NotImplementedError("This method should be overridden.")

    @abstractmethod
    def network_to_str(self, root_node: Optional[str]) -> str:
        """
        Returns a string representation of the whole network with a possibly provided `root_node`.
        """
        raise NotImplementedError("This method should be overridden.")

    @abstractmethod
    def get_file_name(self, root_node: str) -> str:
        """
        Returns the desired file-name of this network.
        """
        raise NotImplementedError("This method should be overridden.")

    @staticmethod
    def model_field_str(model_field: ModelField) -> str:
        """
        Parse the type of the ModelField to a printable string. Copied from pydantic.field.ModelField._type_display()
        """
        result_str = display_as_type(model_field.type_)

        # have to do this since display_as_type(self.outer_type_) is different (and wrong) on python 3.6
        if model_field.shape in MAPPING_LIKE_SHAPES:
            result_str = f"Mapping[{display_as_type(cast(ModelField, model_field.key_field).type_)}, {result_str}]"
        elif model_field.shape == SHAPE_TUPLE:
            result_str = "Tuple[" + ", ".join(
                display_as_type(
                    sub_field.type_ for sub_field in model_field.sub_fields  # type:ignore[arg-type,union-attr]
                )
            )
            result_str += "]"
        elif model_field.shape == SHAPE_GENERIC:
            assert model_field.sub_fields
            result_str = (
                f"{display_as_type(model_field.type_)}["
                f"{', '.join(display_as_type(sub_field.type_) for sub_field in model_field.sub_fields)}]"
            )
        elif model_field.shape != SHAPE_SINGLETON:
            result_str = SHAPE_NAME_LOOKUP[model_field.shape].format(result_str)

        if model_field.allow_none and (model_field.shape != SHAPE_SINGLETON or not model_field.sub_fields):
            result_str = f"Optional[{result_str}]"
        return result_str

    @staticmethod
    def _remove_last_package(namespace: str) -> str:
        return f'{".".join(namespace.split(".")[0:-2])}.{namespace.split(".")[-1]}'


class PlantUMLNetwork(_UMLNetworkABC):
    """
    UML-Network-Parser inheriting from `_UMLNetworkABC`. This subclass parses the network (i.e. itself) into plantuml
    output.
    """

    def _node_to_str(self, node: str, detailed: bool = True, root_node: Optional[str] = None) -> str:
        """
        Parse the class with their fields into a string for plantuml output.
        The class will contain a link to the respective class in the documentation.
        """
        cls_str = (
            f'class "[[{LINK_DOMAIN}/api/bo4e.{node.split(".")[1]}.html#{node}'
            f' {node.split(".")[-1]}]]\\n<size:10>{".".join(node.split(".")[0:-1])}" as {node.split(".")[-1]}'
        )
        if detailed:
            cls_str += " {\n"
            for field in self.nodes[node]["fields"].values():
                type_str = _UMLNetworkABC.model_field_str(field)
                if field.required:
                    cls_str += f"\t{field.alias} : {type_str}\n"
                else:
                    cls_str += f"\t{field.alias} : {type_str} = {field.default}\n"
            cls_str += "}"

        return cls_str

    # pylint: disable=too-many-arguments, too-many-locals
    def _edge_to_str(self, node1: str, node2: str, index: int, detailed: bool, root_node: Optional[str] = None) -> str:
        """
        Parse the connection into a string for plantuml output.
        """
        vert_extension = "{node1} -[norank]-|> {node2} #line:gray"
        horz_extension_lr = "{node1} --|> {node2}"
        horz_extension_rl = "{node2} <|-- {node1}"
        vert_association = "{node1} {card1} -[norank]-* {card2} {node2} #line:gray;text:gray : {field}"
        horz_association_lr = "{node1} {card1} --* {card2} {node2} : {field}"
        horz_association_rl = "{node2} {card2} *-- {card1} {node1} : {field}"

        # The only purpose of this is to use less code below by using the get-method with default values
        association: Dict[Optional[str], str] = {
            node1: horz_association_lr,
            node2: horz_association_rl,
        }
        extension: Dict[Optional[str], str] = {
            node1: horz_extension_lr,
            node2: horz_extension_rl,
        }

        node1_str = _UMLNetworkABC._remove_last_package(node1)
        node2_str = _UMLNetworkABC._remove_last_package(node2)
        if root_node == node1:
            node1_str = "." + node1.split(".")[-1]
        elif root_node == node2:
            node2_str = "." + node2.split(".")[-1]

        if self[node1][node2][index]["type"] == "extension":
            return extension.get(root_node, vert_extension).format(node1=node1_str, node2=node2_str)
        if self[node1][node2][index]["type"] == "association":
            card1 = ""
            card2 = ""
            if detailed:
                # ------ Parse the cardinality into readable strings ---------------------------------------------------
                if self[node1][node2][index]["card1"]:
                    if self[node1][node2][index]["card1"][0] == self[node1][node2][index]["card1"][1]:
                        card1 = f'"{self[node1][node2][index]["card1"][0]}"'
                    else:
                        card1 = f'"{self[node1][node2][index]["card1"][0]}..{self[node1][node2][index]["card1"][1]}"'
                if self[node1][node2][index]["card2"]:
                    if self[node1][node2][index]["card2"][0] == self[node1][node2][index]["card2"][1]:
                        card2 = f'"{self[node1][node2][index]["card2"][0]}"'
                    else:
                        card2 = f'"{self[node1][node2][index]["card2"][0]}..{self[node1][node2][index]["card2"][1]}"'
                # ------------------------------------------------------------------------------------------------------
            return association.get(root_node, vert_association).format(
                node1=node1_str,
                node2=node2_str,
                card1=card1,
                card2=card2,
                field=self[node1][node2][index]["through_field"].alias,
            )
        raise ValueError(
            f"Illegal edge type for plantuml-parser in ['{node1}']['{node2}']['type']: "
            f"{self[node1][node2][index]['type']}"
        )

    def network_to_str(self, root_node: Optional[str]) -> str:
        """
        Build the uml file (content) with class `cls_namespace` treated as root node for this network.
        Classes will be grouped together by namespaces (for instance splitted into `bo` and `com`).
        Only the root node `root_node` will not be included inside its (visual) package namespace.
        """

        regex_pkg = re.compile(r"^bo4e\.(\w+)\.")
        content = "@startuml\nleft to right direction\n\n"
        namespaces: Dict[str, Dict[str, str | bool]] = {}
        # `namespaces` will contain for each package listed in the scope of `pkg` (`pkgs[pkg]["scope"]`) two
        # information:
        # 1. The plantuml-string for the namespaces of the scope containing all respective classes except the root node.
        # 2. A boolean value if there is at least one class in this network in the respective namespace. This is needed
        #    to avoid empty package boxes in the resulting uml-graphs.

        # ------ initialize `namespaces` -------------------------------------------------------------------------------
        for _pkg, value in pkgs.items():
            namespaces[_pkg] = {
                "str": f'namespace "[[{LINK_DOMAIN}/api/bo4e.{_pkg}.html bo4e.{_pkg}'
                f']]" as bo4e.{_pkg} {value["color"]} ' + "{\n",
                "empty": True,
            }
        # ------ build the content strings for each node inside this network -------------------------------------------
        for node in self.nodes:
            _pkg = re.match(regex_pkg, node).group(1)  # type:ignore[union-attr]
            if node == root_node:
                content += self.get_node_str(node, True, True, root_node) + "\n\n"
            else:
                namespaces[_pkg]["str"] += (  # type:ignore[assignment]
                    "\t" + self.get_node_str(node, False, True, root_node) + "\n"  # type:ignore[operator]
                )
                namespaces[_pkg]["empty"] = False
        # ------ add all non-empty namespace-strings to `content` ------------------------------------------------------
        for namespace in namespaces.values():
            if not namespace["empty"]:
                content += namespace["str"] + "}\n"  # type:ignore[operator]
        content += "\n"
        # ------ add all connections to `content` ----------------------------------------------------------------------
        for edge in self.edges:
            content += self.get_edge_str(edge[0], edge[1], edge[2], True, True, root_node) + "\n"
        # ------ Only show fields on the root node ---------------------------------------------------------------------
        if root_node:
            content += "\nhide members\n" f"show .{root_node.split('.')[-1]} fields\n" "@enduml\n"
        # --------------------------------------------------------------------------------------------------------------
        return content

    def get_file_name(self, root_node: str) -> str:
        """
        Returns the desired file name for this network with `root_node` treated as the root_node.
        """
        return root_node.split(".")[-1] + ".puml"


def write_class_umls(uml_network: _UMLNetworkABC, namespaces_to_parse: List[str], output_dir: Path) -> List[Path]:
    """
    Creates an UML graph for every class listed in `namespaces_to_parse` into `[output_dir]/uml/`.
    For each class a separate uml file will be generated. They include this class and its neighbors.
    Additionally, referenced classes will be included only if `regex_incl_network` matches but explicitly excluded if
    `regex_excl_network` matches the namespace of the respective class (e.g. `bo4e.bo.angebot.Angebot`).
    Only relations between the class and its neighbours will be included.
    Currently, only Plantuml is supported as parser.
    Returns a list of created files.
    """
    path_list: List[Path] = []
    for namespace_to_parse in namespaces_to_parse:
        spl = namespace_to_parse.split(".")
        file_path = output_dir / "/".join(spl[0:-2])
        file_name = uml_network.get_file_name(namespace_to_parse)
        uml_subgraph = nx.ego_graph(uml_network, namespace_to_parse, radius=1, undirected=False)
        regex_scope = re.compile(rf'bo4e\.({"|".join(pkgs[spl[1]]["scope"])})\.')
        uml_network_scope = cast(
            _UMLNetworkABC,
            # pylint: disable=cell-var-from-loop
            nx.subgraph_view(
                uml_subgraph,
                filter_node=lambda _node: re.match(regex_scope, _node),
                filter_edge=lambda _node1, _node2, _idx: namespace_to_parse in (_node1, _node2),
            ),
        )
        file_content = uml_network_scope.network_to_str(namespace_to_parse)

        os.makedirs(file_path, exist_ok=True)
        with open(file_path / file_name, "w+", encoding="UTF-8") as uml_file:
            uml_file.write(file_content)
            path_list.append(file_path / file_name)
            # print(f'"{dot_path}{os.path.sep}{dot_file}" created.')
    return path_list


def build_network(module_dir: Path, parser: Type[_UMLNetworkABC]) -> Tuple[_UMLNetworkABC, List[str]]:
    """
    Build a network of the relationships of all classes found in bo4e packages defined by `pkgs` and all classes
    referenced by any class in these packages. Referenced classes will be added only if `regex_incl_network` matches and
    `regex_excl_network` does not match the namespace name of the respective class (e.g. `bo4e.bo.angebot.Angebot`).
    """
    uml_network = parser()
    namespaces_to_parse: List[str] = []
    for pkg in pkgs:
        modls = [name for _, name, _ in pkgutil.iter_modules([str(module_dir / pkg)])]
        for modl_name in modls:
            modl_namespace = f"bo4e.{pkg}.{modl_name}"
            modl = importlib.import_module(modl_namespace)
            # pylint: disable=cell-var-from-loop
            cls_list = inspect.getmembers(
                modl, lambda _member: inspect.isclass(_member) and _member.__module__ == modl_namespace
            )
            for name, cls in cls_list:
                modl_namespace = f"{cls.__module__}.{name}"
                namespaces_to_parse.append(modl_namespace)
                if not uml_network.has_node(modl_namespace):
                    _recursive_add_class(cls, modl_namespace, uml_network)
    return uml_network, namespaces_to_parse


def _recursive_add_class(
    cls_cur: ModelMetaclass,
    modl_namespace: str,
    uml_network: _UMLNetworkABC,
) -> None:
    """
    Add the specified class `cls_cur` to the `uml_network` and recursively add all classes found in fields and
    bases including all matching `regex_incl_network` but excluding all matching 'regex_excl_network'. If both regex
    are conflicting, the respective class will not be added.
    """
    uml_network.add_class(modl_namespace, cls=cls_cur)
    # ------ add base classes to the network which pass `regex_incl_network` and `regex_excl_network` ------------------
    for parent in cls_cur.__bases__:
        type_modl_namespace = f"{parent.__module__}.{parent.__name__}"
        if re.match(regex_incl_network, type_modl_namespace) and not re.match(regex_excl_network, type_modl_namespace):
            if not uml_network.has_node(type_modl_namespace):
                _recursive_add_class(cast(ModelMetaclass, parent), type_modl_namespace, uml_network)
            uml_network.add_extension(
                modl_namespace,
                type_modl_namespace,
            )
    # ------------------------------------------------------------------------------------------------------------------
    # ------ determine references in fields which pass `regex_incl_network` and `regex_excl_network` -------------------
    for model_field in uml_network.nodes[modl_namespace]["fields"].values():
        type_modl_namespace = f"{model_field.type_.__module__}.{model_field.type_.__name__}"
        if re.match(regex_incl_network, type_modl_namespace) and not re.match(regex_excl_network, type_modl_namespace):
            if not uml_network.has_node(type_modl_namespace):
                _recursive_add_class(model_field.type_, type_modl_namespace, uml_network)
            type_str = _UMLNetworkABC.model_field_str(model_field)

            # ------ determine cardinality -----------------------------------------------------------------------------
            card2 = ["1", "1"]
            if type_str.startswith("Optional["):
                card2[0] = "0"
            if type_str.startswith("List[") or type_str.startswith("Optional[List["):
                card2[0] = "0"
                card2[1] = "*"
                if hasattr(model_field.outer_type_, "max_items") and model_field.outer_type_.max_items:
                    card2[1] = str(model_field.outer_type_.max_items)
                if hasattr(model_field.outer_type_, "min_items") and model_field.outer_type_.min_items:
                    card2[0] = str(model_field.outer_type_.min_items)
            # ----------------------------------------------------------------------------------------------------------

            uml_network.add_association(
                modl_namespace,
                type_modl_namespace,
                through_field=model_field,
                card1=None,
                card2=tuple(card2),  # type:ignore[arg-type]
            )
    # ------------------------------------------------------------------------------------------------------------------


def compile_files_kroki(input_dir: Path, output_dir: Path) -> None:
    """
    Compiles all plantuml files inside `input_dir` (recursive) to svg's in `output_dir` with the same subpath as in
    `input_dir`. Files are compiled using web service of [kroki](https://kroki.io)
    """
    url = "https://kroki.io"
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            with open(os.path.join(root, file), "r", encoding="UTF-8") as uml_file:
                x = requests.post(
                    url, json={"diagram_source": uml_file.read(), "diagram_type": "plantuml", "output_format": "svg"}
                )
                subdir = root[len(str(input_dir)) + 1 :]
                os.makedirs(output_dir / subdir, exist_ok=True)
                with open(output_dir / subdir / re.sub(r"\.puml$", ".svg", file), "w+", encoding="UTF-8") as svg_file:
                    svg_file.write(x.text)


def compile_files_plantuml(input_dir: Path, output_dir: Path, executable: Path) -> None:
    """
    Compiles all plantuml files inside `input_dir` (not recursive) to svg's in `output_dir`.
    """
    command = f'java -jar "{executable}" "{input_dir}" -svg -o "{output_dir}"'
    subprocess.call(shlex.split(command))