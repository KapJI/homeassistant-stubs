import yaml
from .const import SECRET_YAML as SECRET_YAML
from .objects import Input as Input, NodeDictClass as NodeDictClass, NodeListClass as NodeListClass, NodeStrClass as NodeStrClass
from _typeshed import Incomplete
from collections.abc import Iterator
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from io import StringIO
from pathlib import Path
from typing import Any, TextIO, TypeVar, overload
from yaml import SafeLoader as FastestAvailableSafeLoader

HAS_C_LOADER: bool
JSON_TYPE: Incomplete
_DictT = TypeVar('_DictT', bound=dict)
_LOGGER: Incomplete

class Secrets:
    config_dir: Incomplete
    _cache: Incomplete
    def __init__(self, config_dir: Path) -> None: ...
    def get(self, requester_path: str, secret: str) -> str: ...
    def _load_secret_yaml(self, secret_dir: Path) -> dict[str, str]: ...

class _LoaderMixin:
    name: str
    stream: Any
    def get_name(self) -> str: ...
    def get_stream_name(self) -> str: ...

class FastSafeLoader(FastestAvailableSafeLoader, _LoaderMixin):
    stream: Incomplete
    name: str
    secrets: Incomplete
    def __init__(self, stream: Any, secrets: Secrets | None = ...) -> None: ...

class PythonSafeLoader(yaml.SafeLoader, _LoaderMixin):
    secrets: Incomplete
    def __init__(self, stream: Any, secrets: Secrets | None = ...) -> None: ...

LoaderType: Incomplete

def load_yaml(fname: str, secrets: Secrets | None = ...) -> JSON_TYPE: ...
def parse_yaml(content: str | TextIO | StringIO, secrets: Secrets | None = ...) -> JSON_TYPE: ...
def _parse_yaml_python(content: str | TextIO | StringIO, secrets: Secrets | None = ...) -> JSON_TYPE: ...
def _parse_yaml(loader: type[FastSafeLoader] | type[PythonSafeLoader], content: str | TextIO, secrets: Secrets | None = ...) -> JSON_TYPE: ...
@overload
def _add_reference(obj: list | NodeListClass, loader: LoaderType, node: yaml.nodes.Node) -> NodeListClass: ...
@overload
def _add_reference(obj: str | NodeStrClass, loader: LoaderType, node: yaml.nodes.Node) -> NodeStrClass: ...
@overload
def _add_reference(obj: _DictT, loader: LoaderType, node: yaml.nodes.Node) -> _DictT: ...
def _include_yaml(loader: LoaderType, node: yaml.nodes.Node) -> JSON_TYPE: ...
def _is_file_valid(name: str) -> bool: ...
def _find_files(directory: str, pattern: str) -> Iterator[str]: ...
def _include_dir_named_yaml(loader: LoaderType, node: yaml.nodes.Node) -> NodeDictClass: ...
def _include_dir_merge_named_yaml(loader: LoaderType, node: yaml.nodes.Node) -> NodeDictClass: ...
def _include_dir_list_yaml(loader: LoaderType, node: yaml.nodes.Node) -> list[JSON_TYPE]: ...
def _include_dir_merge_list_yaml(loader: LoaderType, node: yaml.nodes.Node) -> JSON_TYPE: ...
def _handle_mapping_tag(loader: LoaderType, node: yaml.nodes.MappingNode) -> NodeDictClass: ...
def _construct_seq(loader: LoaderType, node: yaml.nodes.Node) -> JSON_TYPE: ...
def _handle_scalar_tag(loader: LoaderType, node: yaml.nodes.ScalarNode) -> str | int | float | None: ...
def _env_var_yaml(loader: LoaderType, node: yaml.nodes.Node) -> str: ...
def secret_yaml(loader: LoaderType, node: yaml.nodes.Node) -> JSON_TYPE: ...
def add_constructor(tag: Any, constructor: Any) -> None: ...
