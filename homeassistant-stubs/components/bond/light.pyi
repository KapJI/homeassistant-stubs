import abc
from . import BondHub as BondHub
from .const import BPUP_SUBS as BPUP_SUBS, DOMAIN as DOMAIN, HUB as HUB
from .entity import BondEntity as BondEntity
from .utils import BondDevice as BondDevice
from bond_api import BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondBaseLight(BondEntity, LightEntity, metaclass=abc.ABCMeta):
    _attr_supported_features: int

class BondLight(BondBaseLight, BondEntity, LightEntity):
    _attr_supported_features: Any
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions, sub_device: Union[str, None] = ...) -> None: ...
    _attr_is_on: Any
    _attr_brightness: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class BondDownLight(BondBaseLight, BondEntity, LightEntity):
    _attr_is_on: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class BondUpLight(BondBaseLight, BondEntity, LightEntity):
    _attr_is_on: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class BondFireplace(BondEntity, LightEntity):
    _attr_supported_features: Any
    _attr_is_on: Any
    _attr_brightness: Any
    _attr_icon: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
