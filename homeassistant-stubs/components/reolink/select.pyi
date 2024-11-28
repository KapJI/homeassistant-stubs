from .entity import ReolinkChannelCoordinatorEntity as ReolinkChannelCoordinatorEntity, ReolinkChannelEntityDescription as ReolinkChannelEntityDescription, ReolinkChimeCoordinatorEntity as ReolinkChimeCoordinatorEntity, ReolinkChimeEntityDescription as ReolinkChimeEntityDescription
from .util import ReolinkConfigEntry as ReolinkConfigEntry, ReolinkData as ReolinkData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfDataRate as UnitOfDataRate, UnitOfFrequency as UnitOfFrequency
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from reolink_aio.api import Chime as Chime, Host as Host
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ReolinkSelectEntityDescription(SelectEntityDescription, ReolinkChannelEntityDescription):
    get_options: list[str] | Callable[[Host, int], list[str]]
    method: Callable[[Host, int, str], Any]
    value: Callable[[Host, int], str] | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., cmd_key=..., cmd_id=..., supported=..., options=..., get_options, method, value=...) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ReolinkChimeSelectEntityDescription(SelectEntityDescription, ReolinkChimeEntityDescription):
    get_options: list[str]
    method: Callable[[Chime, str], Any]
    value: Callable[[Chime], str]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., cmd_key=..., cmd_id=..., supported=..., options=..., get_options, method, value) -> None: ...

def _get_quick_reply_id(api: Host, ch: int, mess: str) -> int: ...

SELECT_ENTITIES: Incomplete
CHIME_SELECT_ENTITIES: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ReolinkConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ReolinkSelectEntity(ReolinkChannelCoordinatorEntity, SelectEntity):
    entity_description: ReolinkSelectEntityDescription
    _log_error: bool
    _attr_options: Incomplete
    def __init__(self, reolink_data: ReolinkData, channel: int, entity_description: ReolinkSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class ReolinkChimeSelectEntity(ReolinkChimeCoordinatorEntity, SelectEntity):
    entity_description: ReolinkChimeSelectEntityDescription
    _log_error: bool
    _attr_options: Incomplete
    def __init__(self, reolink_data: ReolinkData, chime: Chime, entity_description: ReolinkChimeSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
