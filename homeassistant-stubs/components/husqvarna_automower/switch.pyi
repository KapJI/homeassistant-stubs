from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import EXECUTION_TIME_DELAY as EXECUTION_TIME_DELAY
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerControlEntity as AutomowerControlEntity
from _typeshed import Incomplete
from aioautomower.model import StayOutZones as StayOutZones, Zone as Zone
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerScheduleSwitchEntity(AutomowerControlEntity, SwitchEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class AutomowerStayOutZoneSwitchEntity(AutomowerControlEntity, SwitchEntity):
    _attr_translation_key: str
    coordinator: Incomplete
    stay_out_zone_uid: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, coordinator: AutomowerDataUpdateCoordinator, mower_id: str, stay_out_zone_uid: str) -> None: ...
    @property
    def stay_out_zones(self) -> StayOutZones: ...
    @property
    def stay_out_zone(self) -> Zone: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

def async_remove_entities(hass: HomeAssistant, coordinator: AutomowerDataUpdateCoordinator, entry: AutomowerConfigEntry, mower_id: str) -> None: ...
