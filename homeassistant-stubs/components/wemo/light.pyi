from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity, WemoEntity as WemoEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR, SUPPORT_COLOR_TEMP as SUPPORT_COLOR_TEMP, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import CONNECTION_ZIGBEE as CONNECTION_ZIGBEE
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pywemo.ouimeaux_device import bridge
from typing import Any

SUPPORT_WEMO: Any
WEMO_OFF: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def async_setup_bridge(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, coordinator: DeviceCoordinator) -> None: ...

class WemoLight(WemoEntity, LightEntity):
    light: Any
    _unique_id: Any
    _model_name: Any
    def __init__(self, coordinator: DeviceCoordinator, light: bridge.Light) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def brightness(self) -> int: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def supported_features(self) -> int: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...

class WemoDimmer(WemoBinaryStateEntity, LightEntity):
    @property
    def supported_features(self) -> int: ...
    @property
    def brightness(self) -> int: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...