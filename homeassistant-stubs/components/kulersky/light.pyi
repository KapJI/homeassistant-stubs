import pykulersky
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class KulerskyLight(LightEntity):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_available: bool
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    _light: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, address: str, light: pykulersky.Light) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_rgbw_color: Incomplete
    _attr_brightness: Incomplete
    async def async_update(self) -> None: ...
