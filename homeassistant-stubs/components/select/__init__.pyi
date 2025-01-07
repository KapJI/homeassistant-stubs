from .const import ATTR_CYCLE as ATTR_CYCLE, ATTR_OPTION as ATTR_OPTION, ATTR_OPTIONS as ATTR_OPTIONS, DOMAIN as DOMAIN, SERVICE_SELECT_FIRST as SERVICE_SELECT_FIRST, SERVICE_SELECT_LAST as SERVICE_SELECT_LAST, SERVICE_SELECT_NEXT as SERVICE_SELECT_NEXT, SERVICE_SELECT_OPTION as SERVICE_SELECT_OPTION, SERVICE_SELECT_PREVIOUS as SERVICE_SELECT_PREVIOUS
from _typeshed import Incomplete
from homeassistant.helpers.entity import Entity, EntityDescription
from propcache import cached_property
from typing import Any

__all__ = ['ATTR_CYCLE', 'ATTR_OPTION', 'ATTR_OPTIONS', 'DOMAIN', 'PLATFORM_SCHEMA_BASE', 'PLATFORM_SCHEMA', 'SelectEntity', 'SelectEntityDescription', 'SERVICE_SELECT_FIRST', 'SERVICE_SELECT_LAST', 'SERVICE_SELECT_NEXT', 'SERVICE_SELECT_OPTION', 'SERVICE_SELECT_PREVIOUS']

PLATFORM_SCHEMA: Incomplete
PLATFORM_SCHEMA_BASE: Incomplete

class SelectEntityDescription(EntityDescription, frozen_or_thawed=True):
    options: list[str] | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., options=...) -> None: ...

class SelectEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    _entity_component_unrecorded_attributes: Incomplete
    entity_description: SelectEntityDescription
    _attr_current_option: str | None
    _attr_options: list[str]
    _attr_state: None
    @property
    def capability_attributes(self) -> dict[str, Any]: ...
    @property
    def state(self) -> str | None: ...
    @cached_property
    def options(self) -> list[str]: ...
    @cached_property
    def current_option(self) -> str | None: ...
    def _valid_option_or_raise(self, option: str) -> None: ...
    async def async_handle_select_option(self, option: str) -> None: ...
    def select_option(self, option: str) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    async def async_first(self) -> None: ...
    async def async_last(self) -> None: ...
    async def async_next(self, cycle: bool) -> None: ...
    async def async_previous(self, cycle: bool) -> None: ...
    async def _async_offset_index(self, offset: int, cycle: bool) -> None: ...
    async def _async_select_index(self, idx: int) -> None: ...
