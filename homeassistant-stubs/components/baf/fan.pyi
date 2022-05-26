from .const import DOMAIN as DOMAIN, PRESET_MODE_AUTO as PRESET_MODE_AUTO, SPEED_COUNT as SPEED_COUNT, SPEED_RANGE as SPEED_RANGE
from .entity import BAFEntity as BAFEntity
from .models import BAFData as BAFData
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BAFFan(BAFEntity, FanEntity):
    _attr_supported_features: Incomplete
    _attr_preset_modes: Incomplete
    _attr_speed_count: Incomplete
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
