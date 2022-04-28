from .base_class import TradfriBaseEntity as TradfriBaseEntity
from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, KEY_API as KEY_API
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, ColorMode as ColorMode, LightEntity as LightEntity, LightEntityFeature as LightEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriLight(TradfriBaseEntity, LightEntity):
    _attr_supported_features: Any
    _device_control: Any
    _device_data: Any
    _attr_unique_id: Any
    _hs_color: Any
    _attr_supported_color_modes: Any
    _attr_min_mireds: Any
    _attr_max_mireds: Any
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    def _refresh(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def color_temp(self) -> Union[int, None]: ...
    @property
    def hs_color(self) -> Union[tuple[float, float], None]: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
