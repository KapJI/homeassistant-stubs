from . import WizConfigEntry as WizConfigEntry
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from _typeshed import Incomplete
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import ToggleEntity as ToggleEntity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from pywizlight.bulblibrary import BulbType as BulbType, Features as Features
from typing import Any, ClassVar

PRESET_MODE_BREEZE: str

async def async_setup_entry(hass: HomeAssistant, entry: WizConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WizFanEntity(WizEntity, FanEntity):
    _attr_name: Incomplete
    is_on: ClassVar
    _attr_preset_modes: Incomplete
    _attr_supported_features: Incomplete
    _attr_speed_count: Incomplete
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    _attr_is_on: Incomplete
    _attr_percentage: Incomplete
    _attr_preset_mode: Incomplete
    _attr_current_direction: Incomplete
    @callback
    def _async_update_attrs(self) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
