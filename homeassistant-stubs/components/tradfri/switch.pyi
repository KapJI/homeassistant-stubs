from .base_class import TradfriBaseDevice as TradfriBaseDevice
from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, DEVICES as DEVICES, DOMAIN as DOMAIN, KEY_API as KEY_API
from collections.abc import Callable as Callable
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriSwitch(TradfriBaseDevice, SwitchEntity):
    _attr_unique_id: Any
    def __init__(self, device: Command, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    _device_control: Any
    _device_data: Any
    def _refresh(self, device: Command, write_ha: bool = ...) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
