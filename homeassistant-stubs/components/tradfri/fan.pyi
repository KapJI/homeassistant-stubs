from .base_class import TradfriBaseEntity as TradfriBaseEntity
from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, KEY_API as KEY_API
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

ATTR_AUTO: str
ATTR_MAX_FAN_STEPS: int

def _from_fan_percentage(percentage: int) -> int: ...
def _from_fan_speed(fan_speed: int) -> int: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriAirPurifierFan(TradfriBaseEntity, FanEntity):
    _attr_supported_features: Any
    _device_control: Any
    _device_data: Any
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    def _refresh(self) -> None: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def preset_modes(self) -> Union[list[str], None]: ...
    @property
    def percentage(self) -> Union[int, None]: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_on(self, percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
