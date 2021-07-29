from . import GroupEntity as GroupEntity
from collections.abc import Iterator
from homeassistant.components import light as light
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_COLOR_MODE as ATTR_COLOR_MODE, ATTR_COLOR_TEMP as ATTR_COLOR_TEMP, ATTR_EFFECT as ATTR_EFFECT, ATTR_EFFECT_LIST as ATTR_EFFECT_LIST, ATTR_FLASH as ATTR_FLASH, ATTR_HS_COLOR as ATTR_HS_COLOR, ATTR_MAX_MIREDS as ATTR_MAX_MIREDS, ATTR_MIN_MIREDS as ATTR_MIN_MIREDS, ATTR_RGBWW_COLOR as ATTR_RGBWW_COLOR, ATTR_RGBW_COLOR as ATTR_RGBW_COLOR, ATTR_RGB_COLOR as ATTR_RGB_COLOR, ATTR_SUPPORTED_COLOR_MODES as ATTR_SUPPORTED_COLOR_MODES, ATTR_TRANSITION as ATTR_TRANSITION, ATTR_WHITE_VALUE as ATTR_WHITE_VALUE, ATTR_XY_COLOR as ATTR_XY_COLOR, COLOR_MODE_BRIGHTNESS as COLOR_MODE_BRIGHTNESS, COLOR_MODE_ONOFF as COLOR_MODE_ONOFF, PLATFORM_SCHEMA as PLATFORM_SCHEMA, SUPPORT_EFFECT as SUPPORT_EFFECT, SUPPORT_FLASH as SUPPORT_FLASH, SUPPORT_TRANSITION as SUPPORT_TRANSITION, SUPPORT_WHITE_VALUE as SUPPORT_WHITE_VALUE
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant, State as State
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any, Callable

DEFAULT_NAME: str
SUPPORT_GROUP_LIGHT: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[dict[str, Any], None] = ...) -> None: ...

class LightGroup(GroupEntity, light.LightEntity):
    _attr_available: bool
    _attr_icon: str
    _attr_is_on: bool
    _attr_max_mireds: int
    _attr_min_mireds: int
    _attr_should_poll: bool
    _entity_ids: Any
    _white_value: Any
    _attr_name: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    def __init__(self, unique_id: Union[str, None], name: str, entity_ids: list[str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def white_value(self) -> Union[int, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_brightness: Any
    _attr_hs_color: Any
    _attr_rgb_color: Any
    _attr_rgbw_color: Any
    _attr_rgbww_color: Any
    _attr_xy_color: Any
    _attr_color_temp: Any
    _attr_effect_list: Any
    _attr_effect: Any
    _attr_color_mode: Any
    _attr_supported_color_modes: Any
    _attr_supported_features: int
    async def async_update(self) -> None: ...

def _find_state_attributes(states: list[State], key: str) -> Iterator[Any]: ...
def _mean_int(*args: Any) -> int: ...
def _mean_tuple(*args: Any) -> tuple[Union[float, Any], ...]: ...
def _reduce_attribute(states: list[State], key: str, default: Union[Any, None] = ..., reduce: Callable[..., Any] = ...) -> Any: ...
