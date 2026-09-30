from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.humidifier import HumidifierDeviceClass as HumidifierDeviceClass, HumidifierEntity as HumidifierEntity, HumidifierEntityDescription as HumidifierEntityDescription, HumidifierEntityFeature as HumidifierEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from midealocal.devices.a1 import MideaA1Device
from midealocal.devices.fd import MideaFDDevice
from typing import Any, override

PARALLEL_UPDATES: int
type MideaHumidifierDevice = MideaA1Device | MideaFDDevice

@dataclass(kw_only=True, frozen=True)
class MideaHumidifierEntityDescription(HumidifierEntityDescription):
    models: list[DeviceType]

HUMIDIFIERS: list[MideaHumidifierEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaHumidifier(MideaEntity, HumidifierEntity):
    _device: MideaHumidifierDevice
    entity_description: MideaHumidifierEntityDescription
    _attr_min_humidity: float
    _attr_max_humidity: float
    _attr_supported_features: Incomplete
    def _float_attribute(self, attr: str) -> float | None: ...
    @property
    @override
    def current_humidity(self) -> float | None: ...
    @property
    @override
    def target_humidity(self) -> float | None: ...
    @property
    @override
    def mode(self) -> str | None: ...
    @property
    @override
    def available_modes(self) -> list[str]: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    def set_humidity(self, humidity: int) -> None: ...
    @override
    def set_mode(self, mode: str) -> None: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
