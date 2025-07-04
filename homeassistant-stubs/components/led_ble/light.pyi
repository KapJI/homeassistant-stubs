from .const import DEFAULT_EFFECT_SPEED as DEFAULT_EFFECT_SPEED
from .models import LEDBLEConfigEntry as LEDBLEConfigEntry
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_WHITE as ATTR_WHITE, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from led_ble import LEDBLE as LEDBLE
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: LEDBLEConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LEDBLEEntity(CoordinatorEntity[DataUpdateCoordinator[None]], LightEntity):
    _attr_supported_color_modes: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    _device: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[None], device: LEDBLE, name: str) -> None: ...
    _attr_color_mode: Incomplete
    _attr_brightness: Incomplete
    _attr_rgb_color: Incomplete
    _attr_is_on: Incomplete
    _attr_effect: Incomplete
    _attr_effect_list: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def _async_set_effect(self, effect: str, brightness: int) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def _handle_coordinator_update(self, *args: Any) -> None: ...
    async def async_added_to_hass(self) -> None: ...
