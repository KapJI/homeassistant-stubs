from .const import DEFAULT_WATERING_TIME as DEFAULT_WATERING_TIME, DOMAIN as DOMAIN
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from .entity import HydrawiseEntity as HydrawiseEntity
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydrawise.schema import Zone as Zone
from typing import Any

SWITCH_TYPES: tuple[SwitchEntityDescription, ...]
SWITCH_KEYS: list[str]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HydrawiseSwitch(HydrawiseEntity, SwitchEntity):
    zone: Zone
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _update_attrs(self) -> None: ...
