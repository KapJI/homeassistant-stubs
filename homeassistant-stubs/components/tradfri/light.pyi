from .base_class import TradfriBaseEntity as TradfriBaseEntity
from .const import ATTR_DIMMER as ATTR_DIMMER, ATTR_HUE as ATTR_HUE, ATTR_SAT as ATTR_SAT, ATTR_TRANSITION_TIME as ATTR_TRANSITION_TIME, CONF_GATEWAY_ID as CONF_GATEWAY_ID, CONF_IMPORT_GROUPS as CONF_IMPORT_GROUPS, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, GROUPS_LIST as GROUPS_LIST, KEY_API as KEY_API, SUPPORTED_GROUP_FEATURES as SUPPORTED_GROUP_FEATURES, SUPPORTED_LIGHT_FEATURES as SUPPORTED_LIGHT_FEATURES
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator, TradfriGroupDataUpdateCoordinator as TradfriGroupDataUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_TRANSITION as ATTR_TRANSITION, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR, SUPPORT_COLOR_TEMP as SUPPORT_COLOR_TEMP
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pytradfri.command import Command as Command
from pytradfri.group import Group as Group
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriGroup(CoordinatorEntity, LightEntity):
    _attr_supported_features: Any
    _group: Any
    _api: Any
    _attr_unique_id: Any
    def __init__(self, group_coordinator: TradfriGroupDataUpdateCoordinator, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...

class TradfriLight(TradfriBaseEntity, LightEntity):
    _device_control: Any
    _device_data: Any
    _attr_unique_id: Any
    _hs_color: Any
    _attr_supported_features: Any
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
