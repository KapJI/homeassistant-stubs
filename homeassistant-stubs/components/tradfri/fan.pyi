from .base_class import TradfriBaseDevice as TradfriBaseDevice
from .const import ATTR_AUTO as ATTR_AUTO, CONF_GATEWAY_ID as CONF_GATEWAY_ID, DEVICES as DEVICES, DOMAIN as DOMAIN, KEY_API as KEY_API
from collections.abc import Callable as Callable
from homeassistant.components.fan import FanEntity as FanEntity, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _from_percentage(percentage: int) -> int: ...
def _from_fan_speed(fan_speed: int) -> int: ...

class TradfriAirPurifierFan(TradfriBaseDevice, FanEntity):
    _attr_unique_id: Any
    def __init__(self, device: Command, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    @property
    def supported_features(self) -> int: ...
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
    async def async_turn_on(self, speed: Union[str, None] = ..., percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _device_control: Any
    _device_data: Any
    def _refresh(self, device: Command, write_ha: bool = ...) -> None: ...