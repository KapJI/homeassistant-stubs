from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, UnitOfMass as UnitOfMass, UnitOfTime as UnitOfTime, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from midealocal.device import MideaDevice as MideaDevice
from typing import override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaNumberEntityDescription(NumberEntityDescription):
    models: list[DeviceType]
    max_value_fn: Callable[[MideaDevice], float | None] | None = ...

NUMBERS: list[MideaNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaNumber(MideaEntity, NumberEntity):
    entity_description: MideaNumberEntityDescription
    @property
    @override
    def native_max_value(self) -> float: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    def set_native_value(self, value: float) -> None: ...
