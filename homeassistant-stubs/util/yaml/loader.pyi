import yaml
from .const import SECRET_YAML as SECRET_YAML
from .objects import Input as Input, NodeListClass as NodeListClass, NodeStrClass as NodeStrClass
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from typing import Dict, List, TextIO, TypeVar, Union

JSON_TYPE = Union[List, Dict, str]
DICT_T = TypeVar('DICT_T', bound=Dict)

def clear_secret_cache() -> None: ...

class SafeLineLoader(yaml.SafeLoader):
    def compose_node(self, parent: yaml.nodes.Node, index: int) -> yaml.nodes.Node: ...

def load_yaml(fname: str) -> JSON_TYPE: ...
def parse_yaml(content: Union[str, TextIO]) -> JSON_TYPE: ...
def secret_yaml(loader: SafeLineLoader, node: yaml.nodes.Node) -> JSON_TYPE: ...
