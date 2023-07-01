from . import AbodeAutomation as AbodeAutomation, AbodeDevice as AbodeDevice, AbodeSystem as AbodeSystem
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from jaraco.abode.devices.switch import Switch as AbodeSW
from typing import Any

DEVICE_TYPES: Incomplete
ICON: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AbodeSwitch(AbodeDevice, SwitchEntity):
    _device: AbodeSW
    _attr_name: Incomplete
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...

class AbodeAutomationSwitch(AbodeAutomation, SwitchEntity):
    _attr_icon = ICON
    async def async_added_to_hass(self) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
    def trigger(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
