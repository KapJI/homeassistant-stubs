from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from eheimdigital.classic_vario import EheimDigitalClassicVario
from eheimdigital.device import EheimDigitalDevice
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.components.sensor.const import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Generic, TypeVar, override

PARALLEL_UPDATES: int
_DeviceT_co = TypeVar('_DeviceT_co', bound=EheimDigitalDevice, covariant=True)

@dataclass(frozen=True, kw_only=True)
class EheimDigitalSensorDescription(SensorEntityDescription, Generic[_DeviceT_co]):
    value_fn: Callable[[_DeviceT_co], float | str | None]

CLASSICVARIO_DESCRIPTIONS: tuple[EheimDigitalSensorDescription[EheimDigitalClassicVario], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalSensor(EheimDigitalEntity[_DeviceT_co], SensorEntity, Generic[_DeviceT_co]):
    entity_description: EheimDigitalSensorDescription[_DeviceT_co]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT_co, description: EheimDigitalSensorDescription[_DeviceT_co]) -> None: ...
    _attr_native_value: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
