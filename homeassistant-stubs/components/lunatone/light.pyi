from .const import DOMAIN as DOMAIN
from .coordinator import LunatoneConfigEntry as LunatoneConfigEntry, LunatoneDevicesDataUpdateCoordinator as LunatoneDevicesDataUpdateCoordinator, LunatoneInfoDataUpdateCoordinator as LunatoneInfoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP_KELVIN as ATTR_COLOR_TEMP_KELVIN, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ColorMode as ColorMode, LightEntity as LightEntity, brightness_supported as brightness_supported
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from lunatone_rest_api_client import DALIBroadcast as DALIBroadcast
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: LunatoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LunatoneLight(CoordinatorEntity[LunatoneDevicesDataUpdateCoordinator], LightEntity):
    BRIGHTNESS_SCALE: Incomplete
    _last_brightness: int
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _attr_min_color_temp_kelvin: int
    _attr_max_color_temp_kelvin: int
    _device_id: Incomplete
    _config_entry_unique_id: Incomplete
    _device: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LunatoneDevicesDataUpdateCoordinator, device_id: int, config_entry_unique_id: str) -> None: ...
    @property
    @override
    def device_info(self) -> DeviceInfo: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def brightness(self) -> int | None: ...
    @property
    @override
    def color_mode(self) -> ColorMode: ...
    @property
    @override
    def supported_color_modes(self) -> set[ColorMode]: ...
    @property
    @override
    def color_temp_kelvin(self) -> int | None: ...
    @property
    @override
    def rgb_color(self) -> tuple[int, int, int] | None: ...
    @property
    @override
    def rgbw_color(self) -> tuple[int, int, int, int] | None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class LunatoneLineBroadcastLight(CoordinatorEntity[LunatoneInfoDataUpdateCoordinator], LightEntity):
    BRIGHTNESS_SCALE: Incomplete
    _attr_assumed_state: bool
    _attr_color_mode: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_supported_color_modes: Incomplete
    _coordinator_devices: Incomplete
    _broadcast: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator_info: LunatoneInfoDataUpdateCoordinator, coordinator_devices: LunatoneDevicesDataUpdateCoordinator, broadcast: DALIBroadcast, config_entry_unique_id: str) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
