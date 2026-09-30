from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.water_heater import WaterHeaterEntity as WaterHeaterEntity, WaterHeaterEntityDescription as WaterHeaterEntityDescription, WaterHeaterEntityFeature as WaterHeaterEntityFeature
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_WHOLE as PRECISION_WHOLE, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.device import DeviceType
from midealocal.devices.c3 import MideaC3Device
from midealocal.devices.cd import MideaCDDevice
from midealocal.devices.e2 import MideaE2Device
from midealocal.devices.e3 import MideaE3Device
from midealocal.devices.e6 import DeviceAttributes as E6Attributes, MideaE6Device
from typing import Any, ClassVar, override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaWaterHeaterEntityDescription(WaterHeaterEntityDescription):
    models: list[DeviceType]
    zone: int = ...

WATER_HEATERS: list[MideaWaterHeaterEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
type MideaWaterHeaterDevice = MideaE2Device | MideaE3Device | MideaC3Device | MideaE6Device | MideaCDDevice

class MideaWaterHeater(MideaEntity, WaterHeaterEntity):
    _device: MideaWaterHeaterDevice
    _operations: list[str]
    _attr_supported_features: Incomplete
    _attr_precision: Incomplete
    _attr_temperature_unit: Incomplete
    def __init__(self, device: MideaWaterHeaterDevice, description: MideaWaterHeaterEntityDescription) -> None: ...
    @property
    @override
    def target_temperature_step(self) -> float | None: ...
    @property
    @override
    def current_operation(self) -> str | None: ...
    @property
    @override
    def current_temperature(self) -> float: ...
    @property
    @override
    def target_temperature(self) -> float: ...
    @override
    def set_temperature(self, **kwargs: Any) -> None: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...

class MideaE2WaterHeater(MideaWaterHeater):
    _device: MideaE2Device
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...

class MideaE3WaterHeater(MideaWaterHeater):
    _device: MideaE3Device
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @property
    @override
    def precision(self) -> float: ...

class MideaC3WaterHeater(MideaWaterHeater):
    _device: MideaC3Device
    @property
    @override
    def current_operation(self) -> str: ...
    @property
    @override
    def current_temperature(self) -> float: ...
    @property
    @override
    def target_temperature(self) -> float: ...
    @override
    def set_temperature(self, **kwargs: Any) -> None: ...
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...

class MideaE6WaterHeater(MideaWaterHeater):
    _device: MideaE6Device
    entity_description: MideaWaterHeaterEntityDescription
    _powers: ClassVar[list[E6Attributes]]
    _current_temperatures: ClassVar[list[E6Attributes]]
    _target_temperatures: ClassVar[list[E6Attributes]]
    _power_attr: Incomplete
    _current_temperature_attr: Incomplete
    _target_temperature_attr: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, device: MideaE6Device, description: MideaWaterHeaterEntityDescription) -> None: ...
    @property
    @override
    def current_operation(self) -> str: ...
    @property
    @override
    def current_temperature(self) -> float: ...
    @property
    @override
    def target_temperature(self) -> float: ...
    @override
    def set_temperature(self, **kwargs: Any) -> None: ...
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_away_mode_on(self) -> bool: ...
    @override
    def turn_away_mode_on(self) -> None: ...
    @override
    def turn_away_mode_off(self) -> None: ...

class MideaCDWaterHeater(MideaWaterHeater):
    _device: MideaCDDevice
    @property
    @override
    def min_temp(self) -> float: ...
    @property
    @override
    def max_temp(self) -> float: ...
