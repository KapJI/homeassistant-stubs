from . import EsphomeEntity as EsphomeEntity, EsphomeEnumMapper as EsphomeEnumMapper, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import FanDirection, FanInfo, FanState
from homeassistant.components.fan import DIRECTION_FORWARD as DIRECTION_FORWARD, DIRECTION_REVERSE as DIRECTION_REVERSE, FanEntity as FanEntity, SUPPORT_DIRECTION as SUPPORT_DIRECTION, SUPPORT_OSCILLATE as SUPPORT_OSCILLATE, SUPPORT_SET_SPEED as SUPPORT_SET_SPEED
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item, percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from typing import Any

ORDERED_NAMED_FAN_SPEEDS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_FAN_DIRECTIONS: EsphomeEnumMapper[FanDirection, str]

class EsphomeFan(EsphomeEntity[FanInfo, FanState], FanEntity):
    @property
    def _supports_speed_levels(self) -> bool: ...
    async def async_set_percentage(self, percentage: Union[int, None]) -> None: ...
    async def async_turn_on(self, speed: Union[str, None] = ..., percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_oscillate(self, oscillating: bool) -> None: ...
    async def async_set_direction(self, direction: str) -> None: ...
    def is_on(self) -> Union[bool, None]: ...
    def percentage(self) -> Union[int, None]: ...
    @property
    def speed_count(self) -> int: ...
    def oscillating(self) -> Union[bool, None]: ...
    def current_direction(self) -> Union[str, None]: ...
    @property
    def supported_features(self) -> int: ...
