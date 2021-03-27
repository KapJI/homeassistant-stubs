from homeassistant.const import CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE
from homeassistant.core import split_entity_id as split_entity_id
from typing import Any, Callable, Dict, List

CONF_INCLUDE_DOMAINS: str
CONF_INCLUDE_ENTITY_GLOBS: str
CONF_INCLUDE_ENTITIES: str
CONF_EXCLUDE_DOMAINS: str
CONF_EXCLUDE_ENTITY_GLOBS: str
CONF_EXCLUDE_ENTITIES: str
CONF_ENTITY_GLOBS: str

def convert_filter(config: Dict[str, List[str]]) -> Callable[[str], bool]: ...

BASE_FILTER_SCHEMA: Any
FILTER_SCHEMA: Any

def convert_include_exclude_filter(config: Dict[str, Dict[str, List[str]]]) -> Callable[[str], bool]: ...

INCLUDE_EXCLUDE_FILTER_SCHEMA_INNER: Any
INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA: Any
INCLUDE_EXCLUDE_FILTER_SCHEMA: Any

def generate_filter(include_domains: List[str], include_entities: List[str], exclude_domains: List[str], exclude_entities: List[str], include_entity_globs: List[str]=..., exclude_entity_globs: List[str]=...) -> Callable[[str], bool]: ...
