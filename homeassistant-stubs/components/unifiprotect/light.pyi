from .const import DOMAIN as DOMAIN
from .data import ProtectData as ProtectData
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyunifiprotect.data import Light as Light
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def unifi_brightness_to_hass(value: int) -> int: ...
def hass_to_unifi_brightness(value: int) -> int: ...

class ProtectLight(ProtectDeviceEntity, LightEntity):
    device: Light
    _attr_icon: str
    _attr_supported_features: Any
    _attr_is_on: Any
    _attr_brightness: Any
    def _async_update_device_from_protect(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
