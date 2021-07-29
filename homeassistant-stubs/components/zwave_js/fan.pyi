from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .discovery import ZwaveDiscoveryInfo as ZwaveDiscoveryInfo
from .entity import ZWaveBaseEntity as ZWaveBaseEntity
from homeassistant.components.fan import FanEntity as FanEntity, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import int_states_in_range as int_states_in_range, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

SUPPORTED_FEATURES = SUPPORT_SET_SPEED
SPEED_RANGE: Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ZwaveFan(ZWaveBaseEntity, FanEntity):
    async def async_set_percentage(self, percentage: Union[int, None]) -> None: ...
    async def async_turn_on(self, speed: Union[str, None] = ..., percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def percentage(self) -> Union[int, None]: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def supported_features(self) -> int: ...
