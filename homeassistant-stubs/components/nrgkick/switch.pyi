from .coordinator import NRGkickConfigEntry as NRGkickConfigEntry, NRGkickData as NRGkickData, NRGkickDataUpdateCoordinator as NRGkickDataUpdateCoordinator
from .entity import NRGkickEntity as NRGkickEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

PARALLEL_UPDATES: int
CHARGING_ENABLED_KEY: str

def _is_charging_enabled(data: NRGkickData) -> bool: ...
async def async_setup_entry(_hass: HomeAssistant, entry: NRGkickConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NRGkickChargingEnabledSwitch(NRGkickEntity, SwitchEntity):
    _attr_translation_key = CHARGING_ENABLED_KEY
    def __init__(self, coordinator: NRGkickDataUpdateCoordinator) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
