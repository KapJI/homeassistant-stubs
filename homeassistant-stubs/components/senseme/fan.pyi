from .const import DOMAIN as DOMAIN, PRESET_MODE_WHOOSH as PRESET_MODE_WHOOSH, SENSEME_DIRECTION_FORWARD as SENSEME_DIRECTION_FORWARD, SENSEME_DIRECTION_REVERSE as SENSEME_DIRECTION_REVERSE
from .entity import SensemeEntity as SensemeEntity
from _typeshed import Incomplete
from aiosenseme import SensemeFan as SensemeFan
from homeassistant import config_entries as config_entries
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

SENSEME_DIRECTION_TO_HASS: Incomplete
HASS_DIRECTION_TO_SENSEME: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HASensemeFan(SensemeEntity, FanEntity):
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: SensemeFan) -> None: ...
    _attr_is_on: Incomplete
    _attr_current_direction: Incomplete
    _attr_percentage: Incomplete
    _attr_preset_mode: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
