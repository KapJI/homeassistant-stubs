from . import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator, ValloxEntity as ValloxEntity
from .const import DOMAIN as DOMAIN, METRIC_KEY_MODE as METRIC_KEY_MODE, METRIC_KEY_PROFILE_FAN_SPEED_AWAY as METRIC_KEY_PROFILE_FAN_SPEED_AWAY, METRIC_KEY_PROFILE_FAN_SPEED_BOOST as METRIC_KEY_PROFILE_FAN_SPEED_BOOST, METRIC_KEY_PROFILE_FAN_SPEED_HOME as METRIC_KEY_PROFILE_FAN_SPEED_HOME, MODE_OFF as MODE_OFF, MODE_ON as MODE_ON, STR_TO_VALLOX_PROFILE_SETTABLE as STR_TO_VALLOX_PROFILE_SETTABLE, VALLOX_PROFILE_TO_STR_SETTABLE as VALLOX_PROFILE_TO_STR_SETTABLE
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature, NotValidPresetModeError as NotValidPresetModeError
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, NamedTuple
from vallox_websocket_api import Vallox as Vallox

_LOGGER: Incomplete

class ExtraStateAttributeDetails(NamedTuple):
    description: str
    metric_key: str

EXTRA_STATE_ATTRIBUTES: Incomplete

def _convert_fan_speed_value(value: StateType) -> Union[int, None]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ValloxFanEntity(ValloxEntity, FanEntity):
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, client: Vallox, coordinator: ValloxDataUpdateCoordinator) -> None: ...
    @property
    def preset_modes(self) -> list[str]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def preset_mode(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Union[int, None]]: ...
    async def _async_set_preset_mode_internal(self, preset_mode: str) -> bool: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_on(self, percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
