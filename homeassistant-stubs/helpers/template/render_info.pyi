import collections.abc
from . import Template as Template
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from contextvars import ContextVar
from homeassistant.core import split_entity_id as split_entity_id
from homeassistant.exceptions import TemplateError as TemplateError

ALL_STATES_RATE_LIMIT: int
DOMAIN_STATES_RATE_LIMIT: int
render_info_cv: ContextVar[RenderInfo | None]

def _true(entity_id: str) -> bool: ...
def _false(entity_id: str) -> bool: ...

class RenderInfo:
    __slots__: Incomplete
    template: Incomplete
    filter_lifecycle: Callable[[str], bool]
    filter: Callable[[str], bool]
    _result: str | None
    is_static: bool
    exception: TemplateError | None
    all_states: bool
    all_states_lifecycle: bool
    domains: collections.abc.Set[str]
    domains_lifecycle: collections.abc.Set[str]
    entities: collections.abc.Set[str]
    rate_limit: float | None
    has_time: bool
    def __init__(self, template: Template) -> None: ...
    def __repr__(self) -> str: ...
    def _filter_domains_and_entities(self, entity_id: str) -> bool: ...
    def _filter_entities(self, entity_id: str) -> bool: ...
    def _filter_lifecycle_domains(self, entity_id: str) -> bool: ...
    def result(self) -> str: ...
    def _freeze_static(self) -> None: ...
    def _freeze_sets(self) -> None: ...
    def _freeze(self) -> None: ...
