from . import TPLinkConfigEntry as TPLinkConfigEntry, legacy_device_id as legacy_device_id
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkModuleEntity as CoordinatedTPLinkModuleEntity, TPLinkModuleEntityDescription as TPLinkModuleEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from homeassistant.util.scaling import int_states_in_range as int_states_in_range
from kasa import Device as Device
from typing import Any

PARALLEL_UPDATES: int
_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class TPLinkFanEntityDescription(FanEntityDescription, TPLinkModuleEntityDescription):
    unique_id_fn: Callable[[Device, TPLinkModuleEntityDescription], str] = ...

FAN_DESCRIPTIONS: tuple[TPLinkFanEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

SPEED_RANGE: Incomplete

class TPLinkFanEntity(CoordinatedTPLinkModuleEntity, FanEntity):
    _attr_speed_count: Incomplete
    _attr_supported_features: Incomplete
    entity_description: TPLinkFanEntityDescription
    fan_module: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkFanEntityDescription, *, parent: Device | None = None) -> None: ...
    @async_refresh_after
    async def async_turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    _attr_is_on: Incomplete
    _attr_percentage: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
