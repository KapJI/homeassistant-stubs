from .const import DEFAULT_BRAND as DEFAULT_BRAND, DOMAIN as DOMAIN
from .data import ProtectData as ProtectData, ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import ProtectDeviceEntity as ProtectDeviceEntity
from .utils import async_ufp_instance_command as async_ufp_instance_command
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override
from uiprotect.data import Light, ProtectAdoptableDeviceModel as ProtectAdoptableDeviceModel, PublicDeviceModel as PublicDeviceModel
from uiprotect.data.public_devices import PublicLight

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
    _ufp_uses_public: bool
    _private: Incomplete
    _ufp_public_obj: Incomplete
    def __init__(self, data: ProtectData, public: PublicLight | None, private: Light | None) -> None: ...
    _attr_device_info: Incomplete
    @callback
    @override
    def _async_set_device_info(self) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    @callback
    @override
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
    def _public_or_raise(self) -> PublicLight: ...
    @async_ufp_instance_command
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_ufp_instance_command
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
