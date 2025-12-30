from . import UnifiConfigEntry as UnifiConfigEntry
from .entity import UnifiEntity as UnifiEntity, UnifiEntityDescription as UnifiEntityDescription, async_device_available_fn as async_device_available_fn, async_device_device_info_fn as async_device_device_info_fn
from .hub import UnifiHub as UnifiHub
from _typeshed import Incomplete
from aiounifi.interfaces.api_handlers import APIHandler as APIHandler, ItemEvent
from aiounifi.models.api import ApiItem as ApiItem
from aiounifi.models.device import Device
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityDescription as LightEntityDescription, LightEntityFeature as LightEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.color import rgb_hex_to_rgb_list as rgb_hex_to_rgb_list
from typing import Any

def convert_brightness_to_unifi(ha_brightness: int) -> int: ...
def convert_brightness_to_ha(unifi_brightness: int) -> int: ...
def get_device_brightness_or_default(device: Device) -> int: ...
@callback
def async_device_led_supported_fn(hub: UnifiHub, obj_id: str) -> bool: ...
@callback
def async_device_led_is_on_fn(hub: UnifiHub, device: Device) -> bool: ...
async def async_device_led_control_fn(hub: UnifiHub, obj_id: str, turn_on: bool, **kwargs: Any) -> None: ...

@dataclass(frozen=True, kw_only=True)
class UnifiLightEntityDescription[HandlerT: APIHandler, ApiItemT: ApiItem](LightEntityDescription, UnifiEntityDescription[HandlerT, ApiItemT]):
    control_fn: Callable[[UnifiHub, str, bool], Coroutine[Any, Any, None]]
    is_on_fn: Callable[[UnifiHub, ApiItemT], bool]

ENTITY_DESCRIPTIONS: tuple[UnifiLightEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: UnifiConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiLightEntity[HandlerT: APIHandler, ApiItemT: ApiItem](UnifiEntity[HandlerT, ApiItemT], LightEntity):
    entity_description: UnifiLightEntityDescription[HandlerT, ApiItemT]
    _attr_supported_features: Incomplete
    _attr_supported_color_modes: Incomplete
    _attr_color_mode: Incomplete
    @callback
    def async_initiate_state(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    _attr_brightness: Incomplete
    _attr_rgb_color: Incomplete
    @callback
    def async_update_state(self, event: ItemEvent, obj_id: str) -> None: ...
