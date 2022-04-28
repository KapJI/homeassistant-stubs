import abc
from .const import ATTR_POWER_STATE as ATTR_POWER_STATE, BPUP_SUBS as BPUP_SUBS, DOMAIN as DOMAIN, HUB as HUB, SERVICE_SET_LIGHT_BRIGHTNESS_TRACKED_STATE as SERVICE_SET_LIGHT_BRIGHTNESS_TRACKED_STATE, SERVICE_SET_LIGHT_POWER_TRACKED_STATE as SERVICE_SET_LIGHT_POWER_TRACKED_STATE
from .entity import BondEntity as BondEntity
from .utils import BondDevice as BondDevice, BondHub as BondHub
from bond_api import BPUPSubscriptions as BPUPSubscriptions
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any
SERVICE_START_INCREASING_BRIGHTNESS: str
SERVICE_START_DECREASING_BRIGHTNESS: str
SERVICE_STOP: str
ENTITY_SERVICES: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BondBaseLight(BondEntity, LightEntity, metaclass=abc.ABCMeta):
    _attr_color_mode: Any
    _attr_supported_color_modes: Any
    async def async_set_brightness_belief(self, brightness: int) -> None: ...
    async def async_set_power_belief(self, power_state: bool) -> None: ...

class BondLight(BondBaseLight, BondEntity, LightEntity):
    _attr_color_mode: Any
    _attr_supported_color_modes: Any
    def __init__(self, hub: BondHub, device: BondDevice, bpup_subs: BPUPSubscriptions, sub_device: Union[str, None] = ...) -> None: ...
    _attr_is_on: Any
    _attr_brightness: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def _async_has_action_or_raise(self, action: str) -> None: ...
    async def async_start_increasing_brightness(self) -> None: ...
    async def async_start_decreasing_brightness(self) -> None: ...
    async def async_stop(self) -> None: ...

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
    _attr_color_mode: Any
    _attr_supported_color_modes: Any
    _attr_is_on: Any
    _attr_brightness: Any
    _attr_icon: Any
    def _apply_state(self, state: dict) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_brightness_belief(self, brightness: int) -> None: ...
    async def async_set_power_belief(self, power_state: bool) -> None: ...
