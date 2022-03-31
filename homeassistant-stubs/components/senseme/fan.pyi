from .const import DOMAIN as DOMAIN, PRESET_MODE_WHOOSH as PRESET_MODE_WHOOSH, SENSEME_DIRECTION_FORWARD as SENSEME_DIRECTION_FORWARD, SENSEME_DIRECTION_REVERSE as SENSEME_DIRECTION_REVERSE
from .entity import SensemeEntity as SensemeEntity
from aiosenseme import SensemeFan as SensemeFan
from homeassistant import config_entries as config_entries
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, SUPPORT_DIRECTION as SUPPORT_DIRECTION, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

SENSEME_DIRECTION_TO_HASS: Any
HASS_DIRECTION_TO_SENSEME: Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class HASensemeFan(SensemeEntity, FanEntity):
    _attr_supported_features: Any
    _attr_preset_modes: Any
    _attr_speed_count: Any
    _attr_unique_id: Any
    def __init__(self, device: SensemeFan) -> None: ...
    _attr_is_on: Any
    _attr_current_direction: Any
    _attr_percentage: Any
    _attr_preset_mode: Any
    def _async_update_attrs(self) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
