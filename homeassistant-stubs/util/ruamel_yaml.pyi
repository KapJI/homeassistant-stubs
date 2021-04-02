from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.yaml import secret_yaml as secret_yaml
from ruamel.yaml.constructor import SafeConstructor
from typing import Dict, List, Union

JSON_TYPE = Union[List, Dict, str]

class ExtSafeConstructor(SafeConstructor):
    name: Union[str, None] = ...

class UnsupportedYamlError(HomeAssistantError): ...
class WriteError(HomeAssistantError): ...

def object_to_yaml(data: JSON_TYPE) -> str: ...
def yaml_to_object(data: str) -> JSON_TYPE: ...
def load_yaml(fname: str, round_trip: bool=...) -> JSON_TYPE: ...
def save_yaml(fname: str, data: JSON_TYPE) -> None: ...