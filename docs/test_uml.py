from pathlib import Path

from docs.uml import PlantUMLNetwork, build_network


def test_network_build() -> None:
    """
    This test is only for debugging purposes.
    """
    project_root_dir = Path(__file__).parent.parent
    module_dir = project_root_dir / "src/bo4e"
    _network, _namespaces_to_parse = build_network(module_dir, PlantUMLNetwork)
