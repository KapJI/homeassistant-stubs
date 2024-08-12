from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity, ISYProgramEntity as ISYProgramEntity
from .models import IsyData as IsyData
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from typing import Any

SPEED_RANGE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ISYFanEntity(ISYNodeEntity, FanEntity):
    _attr_supported_features: Incomplete
    _enable_turn_on_off_backwards_compatibility: bool
    @property
    def percentage(self) -> int | None: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...

class ISYFanProgramEntity(ISYProgramEntity, FanEntity):
    @property
    def percentage(self) -> int | None: ...
    @property
    def speed_count(self) -> int: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
