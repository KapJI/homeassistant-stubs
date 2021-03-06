from . import get_hyperion_device_id as get_hyperion_device_id, get_hyperion_unique_id as get_hyperion_unique_id, listen_for_instance_updates as listen_for_instance_updates
from .const import CONF_EFFECT_HIDE_LIST as CONF_EFFECT_HIDE_LIST, CONF_INSTANCE_CLIENTS as CONF_INSTANCE_CLIENTS, CONF_PRIORITY as CONF_PRIORITY, DEFAULT_ORIGIN as DEFAULT_ORIGIN, DEFAULT_PRIORITY as DEFAULT_PRIORITY, DOMAIN as DOMAIN, HYPERION_MANUFACTURER_NAME as HYPERION_MANUFACTURER_NAME, HYPERION_MODEL_NAME as HYPERION_MODEL_NAME, NAME_SUFFIX_HYPERION_LIGHT as NAME_SUFFIX_HYPERION_LIGHT, NAME_SUFFIX_HYPERION_PRIORITY_LIGHT as NAME_SUFFIX_HYPERION_PRIORITY_LIGHT, SIGNAL_ENTITY_REMOVE as SIGNAL_ENTITY_REMOVE, TYPE_HYPERION_LIGHT as TYPE_HYPERION_LIGHT, TYPE_HYPERION_PRIORITY_LIGHT as TYPE_HYPERION_PRIORITY_LIGHT
from collections.abc import Sequence
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_EFFECT as ATTR_EFFECT, ATTR_HS_COLOR as ATTR_HS_COLOR, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_COLOR as SUPPORT_COLOR, SUPPORT_EFFECT as SUPPORT_EFFECT
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from hyperion import client as client
from types import MappingProxyType
from typing import Any

_LOGGER: Any
COLOR_BLACK: Any
CONF_DEFAULT_COLOR: str
CONF_HDMI_PRIORITY: str
CONF_EFFECT_LIST: str
KEY_EFFECT_SOLID: str
DEFAULT_COLOR: Any
DEFAULT_BRIGHTNESS: int
DEFAULT_EFFECT = KEY_EFFECT_SOLID
DEFAULT_NAME: str
DEFAULT_PORT: Any
DEFAULT_HDMI_PRIORITY: int
DEFAULT_EFFECT_LIST: list[str]
SUPPORT_HYPERION: Any
ICON_LIGHTBULB: str
ICON_EFFECT: str
ICON_EXTERNAL_SOURCE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> bool: ...

class HyperionBaseLight(LightEntity):
    _unique_id: Any
    _name: Any
    _device_id: Any
    _instance_name: Any
    _options: Any
    _client: Any
    _brightness: int
    _rgb_color: Any
    _effect: Any
    _static_effect_list: Any
    _effect_list: Any
    _client_callbacks: Any
    def __init__(self, server_id: str, instance_num: int, instance_name: str, options: MappingProxyType[str, Any], hyperion_client: client.HyperionClient) -> None: ...
    def _compute_unique_id(self, server_id: str, instance_num: int) -> str: ...
    def _compute_name(self, instance_name: str) -> str: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def brightness(self) -> int: ...
    @property
    def hs_color(self) -> tuple[float, float]: ...
    @property
    def icon(self) -> str: ...
    @property
    def effect(self) -> str: ...
    @property
    def effect_list(self) -> list[str]: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    def _get_option(self, key: str) -> Any: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    def _set_internal_state(self, brightness: Union[int, None] = ..., rgb_color: Union[Sequence[int], None] = ..., effect: Union[str, None] = ...) -> None: ...
    def _update_components(self, _: Union[dict[str, Any], None] = ...) -> None: ...
    def _update_adjustment(self, _: Union[dict[str, Any], None] = ...) -> None: ...
    def _update_priorities(self, _: Union[dict[str, Any], None] = ...) -> None: ...
    def _update_effect_list(self, _: Union[dict[str, Any], None] = ...) -> None: ...
    def _update_full_state(self) -> None: ...
    def _update_client(self, _: Union[dict[str, Any], None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def _support_external_effects(self) -> bool: ...
    def _get_priority_entry_that_dictates_state(self) -> Union[dict[str, Any], None]: ...
    def _allow_priority_update(self, priority: Union[dict[str, Any], None] = ...) -> bool: ...

class HyperionLight(HyperionBaseLight):
    def _compute_unique_id(self, server_id: str, instance_num: int) -> str: ...
    def _compute_name(self, instance_name: str) -> str: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class HyperionPriorityLight(HyperionBaseLight):
    def _compute_unique_id(self, server_id: str, instance_num: int) -> str: ...
    def _compute_name(self, instance_name: str) -> str: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def _support_external_effects(self) -> bool: ...
    def _get_priority_entry_that_dictates_state(self) -> Union[dict[str, Any], None]: ...
    @classmethod
    def _is_priority_entry_black(cls, priority: Union[dict[str, Any], None]) -> bool: ...
    def _allow_priority_update(self, priority: Union[dict[str, Any], None] = ...) -> bool: ...

LIGHT_TYPES: Any
