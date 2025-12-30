from .data import ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from .utils import async_ufp_instance_command as async_ufp_instance_command
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any
from uiprotect.data import Light as Light, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def unifi_brightness_to_hass(value: int) -> int: ...
def hass_to_unifi_brightness(value: int) -> int: ...

class ProtectLight(ProtectDeviceEntity, LightEntity):
    device: Light
    _attr_icon: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _state_attrs: Incomplete
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    @async_ufp_instance_command
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_ufp_instance_command
    async def async_turn_off(self, **kwargs: Any) -> None: ...
