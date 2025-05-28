from . import HomeeConfigEntry as HomeeConfigEntry
from .const import DOMAIN as DOMAIN, PRESET_AUTO as PRESET_AUTO, PRESET_MANUAL as PRESET_MANUAL, PRESET_SUMMER as PRESET_SUMMER
from .entity import HomeeNodeEntity as HomeeNodeEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from pyHomee.model import HomeeAttribute, HomeeNode as HomeeNode
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: HomeeConfigEntry, async_add_devices: AddConfigEntryEntitiesCallback) -> None: ...

class HomeeFan(HomeeNodeEntity, FanEntity):
    _attr_translation_key = DOMAIN
    _attr_name: Incomplete
    _attr_preset_modes: Incomplete
    speed_range: Incomplete
    _attr_speed_count: Incomplete
    _speed_attribute: HomeeAttribute
    _mode_attribute: HomeeAttribute
    def __init__(self, node: HomeeNode, entry: HomeeConfigEntry) -> None: ...
    @property
    def supported_features(self) -> FanEntityFeature: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def percentage(self) -> int: ...
    @property
    def preset_mode(self) -> str: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_set_preset_mode(self, preset_mode: str) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
