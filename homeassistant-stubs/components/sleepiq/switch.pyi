from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData, SleepIQPauseUpdateCoordinator as SleepIQPauseUpdateCoordinator
from .entity import SleepIQBedCoordinator as SleepIQBedCoordinator
from asyncsleepiq import SleepIQBed as SleepIQBed
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepNumberPrivateSwitch(SleepIQBedCoordinator, SwitchEntity):
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, coordinator: SleepIQPauseUpdateCoordinator, bed: SleepIQBed) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
