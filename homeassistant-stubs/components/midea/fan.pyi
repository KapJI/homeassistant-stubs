from .const import PRESET_MODE_NONE as PRESET_MODE_NONE
from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityDescription as FanEntityDescription, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.percentage import percentage_to_ranged_value as percentage_to_ranged_value, ranged_value_to_percentage as ranged_value_to_percentage
from midealocal.const import DeviceType
from midealocal.devices.b6 import MideaB6Device
from midealocal.devices.ce import MideaCEDevice
from midealocal.devices.fa import MideaFADevice
from midealocal.devices.x40 import MideaX40Device
from typing import Any, override

PARALLEL_UPDATES: int
type MideaFanDevice = MideaFADevice | MideaB6Device | MideaCEDevice | MideaX40Device
type MideaCombinedTurnOnDevice = MideaFADevice | MideaB6Device

@dataclass(kw_only=True, frozen=True)
class MideaFanEntityDescription(FanEntityDescription):
    models: list[DeviceType]
    supported_features: FanEntityFeature
    has_combined_turn_on: bool = ...
    is_on_attribute: str

FANS: list[MideaFanEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaFan(MideaEntity, FanEntity):
    _device: MideaFanDevice
    entity_description: MideaFanEntityDescription
    _attr_supported_features: Incomplete
    _attr_speed_count: Incomplete
    _attr_preset_modes: Incomplete
    def __init__(self, device: MideaFanDevice, description: MideaFanEntityDescription) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @property
    @override
    def preset_mode(self) -> str | None: ...
    @property
    @override
    def percentage(self) -> int | None: ...
    @property
    @override
    def oscillating(self) -> bool | None: ...
    @override
    def oscillate(self, oscillating: bool) -> None: ...
    @override
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @override
    def set_percentage(self, percentage: int) -> None: ...
    @override
    async def async_set_percentage(self, percentage: int) -> None: ...
    @override
    def set_preset_mode(self, preset_mode: str) -> None: ...
