from . import ValloxStateProxy as ValloxStateProxy
from .const import DOMAIN as DOMAIN, METRIC_KEY_MODE as METRIC_KEY_MODE, METRIC_KEY_PROFILE_FAN_SPEED_AWAY as METRIC_KEY_PROFILE_FAN_SPEED_AWAY, METRIC_KEY_PROFILE_FAN_SPEED_BOOST as METRIC_KEY_PROFILE_FAN_SPEED_BOOST, METRIC_KEY_PROFILE_FAN_SPEED_HOME as METRIC_KEY_PROFILE_FAN_SPEED_HOME, MODE_OFF as MODE_OFF, MODE_ON as MODE_ON, SIGNAL_VALLOX_STATE_UPDATE as SIGNAL_VALLOX_STATE_UPDATE, STR_TO_VALLOX_PROFILE_SETTABLE as STR_TO_VALLOX_PROFILE_SETTABLE, VALLOX_PROFILE_TO_STR_SETTABLE as VALLOX_PROFILE_TO_STR_SETTABLE
from collections.abc import Mapping
from homeassistant.components.fan import FanEntity as FanEntity, NotValidPresetModeError as NotValidPresetModeError, SUPPORT_PRESET_MODE as SUPPORT_PRESET_MODE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from vallox_websocket_api import Vallox as Vallox

_LOGGER: Any
ATTR_PROFILE_FAN_SPEED_HOME: Any
ATTR_PROFILE_FAN_SPEED_AWAY: Any
ATTR_PROFILE_FAN_SPEED_BOOST: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ValloxFan(FanEntity):
    _attr_should_poll: bool
    _client: Any
    _state_proxy: Any
    _is_on: bool
    _preset_mode: Any
    _fan_speed_home: Any
    _fan_speed_away: Any
    _fan_speed_boost: Any
    _attr_name: Any
    _attr_available: bool
    def __init__(self, name: str, client: Vallox, state_proxy: ValloxStateProxy) -> None: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def preset_modes(self) -> list[str]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Union[int, None]]: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...
    async def async_update(self) -> None: ...
    async def _async_set_preset_mode_internal(self, preset_mode: str) -> bool: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_on(self, speed: Union[str, None] = ..., percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
