from .models import States as States
from _typeshed import Incomplete
from homeassistant.const import CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_EXCLUDE as CONF_EXCLUDE, CONF_INCLUDE as CONF_INCLUDE
from homeassistant.helpers.entityfilter import CONF_ENTITY_GLOBS as CONF_ENTITY_GLOBS
from homeassistant.helpers.typing import ConfigType as ConfigType
from sqlalchemy.sql.elements import ClauseList as ClauseList

DOMAIN: str
HISTORY_FILTERS: str
GLOB_TO_SQL_CHARS: Incomplete

def sqlalchemy_filter_from_include_exclude_conf(conf: ConfigType) -> Union[Filters, None]: ...

class Filters:
    excluded_entities: Incomplete
    excluded_domains: Incomplete
    excluded_entity_globs: Incomplete
    included_entities: Incomplete
    included_domains: Incomplete
    included_entity_globs: Incomplete
    def __init__(self) -> None: ...
    @property
    def has_config(self) -> bool: ...
    def entity_filter(self) -> ClauseList: ...

def _glob_to_like(glob_str: str) -> ClauseList: ...
