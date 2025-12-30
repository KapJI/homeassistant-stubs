from .const import DOMAIN as DOMAIN
from .coordinator import LunatoneConfigEntry as LunatoneConfigEntry, LunatoneDevicesDataUpdateCoordinator as LunatoneDevicesDataUpdateCoordinator, LunatoneInfoDataUpdateCoordinator as LunatoneInfoDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity, brightness_supported as brightness_supported
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util.color import brightness_to_value as brightness_to_value, value_to_brightness as value_to_brightness
from lunatone_rest_api_client import DALIBroadcast as DALIBroadcast
from typing import Any

PARALLEL_UPDATES: int
STATUS_UPDATE_DELAY: float

async def async_setup_entry(hass: HomeAssistant, config_entry: LunatoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LunatoneLight(CoordinatorEntity[LunatoneDevicesDataUpdateCoordinator], LightEntity):
    BRIGHTNESS_SCALE: Incomplete
    _last_brightness: int
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_should_poll: bool
    _device_id: Incomplete
    _interface_serial_number: Incomplete
    _device: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LunatoneDevicesDataUpdateCoordinator, device_id: int, interface_serial_number: int) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> int: ...
    @property
    def color_mode(self) -> ColorMode: ...
    @property
    def supported_color_modes(self) -> set[ColorMode]: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class LunatoneLineBroadcastLight(CoordinatorEntity[LunatoneInfoDataUpdateCoordinator], LightEntity):
    BRIGHTNESS_SCALE: Incomplete
    _attr_assumed_state: bool
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _coordinator_devices: Incomplete
    _broadcast: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator_info: LunatoneInfoDataUpdateCoordinator, coordinator_devices: LunatoneDevicesDataUpdateCoordinator, broadcast: DALIBroadcast) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
