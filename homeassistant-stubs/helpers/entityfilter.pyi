from homeassistant.const import CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE
from homeassistant.core import split_entity_id as split_entity_id
from typing import Any, Callable, Pattern

CONF_INCLUDE_DOMAINS: str
CONF_INCLUDE_ENTITY_GLOBS: str
CONF_INCLUDE_ENTITIES: str
CONF_EXCLUDE_DOMAINS: str
CONF_EXCLUDE_ENTITY_GLOBS: str
CONF_EXCLUDE_ENTITIES: str
CONF_ENTITY_GLOBS: str

def convert_filter(config: dict[str, list[str]]) -> Callable[[str], bool]: ...

BASE_FILTER_SCHEMA: Any
FILTER_SCHEMA: Any

def convert_include_exclude_filter(config: dict[str, dict[str, list[str]]]) -> Callable[[str], bool]: ...

INCLUDE_EXCLUDE_FILTER_SCHEMA_INNER: Any
INCLUDE_EXCLUDE_BASE_FILTER_SCHEMA: Any
INCLUDE_EXCLUDE_FILTER_SCHEMA: Any

def _glob_to_re(glob: str) -> Pattern[str]: ...
def _test_against_patterns(patterns: list[Pattern[str]], entity_id: str) -> bool: ...
def generate_filter(include_domains: list[str], include_entities: list[str], exclude_domains: list[str], exclude_entities: list[str], include_entity_globs: list[str]=..., exclude_entity_globs: list[str]=...) -> Callable[[str], bool]: ...
