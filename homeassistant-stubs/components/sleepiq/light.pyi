from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData
from .entity import SleepIQBedEntity as SleepIQBedEntity
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQLight as SleepIQLight
from homeassistant.components.light import LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQLightEntity(SleepIQBedEntity, LightEntity):
    light: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, bed: SleepIQBed, light: SleepIQLight) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Any
    def _async_update_attrs(self) -> None: ...
