from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from eheimdigital.classic_vario import EheimDigitalClassicVario
from eheimdigital.device import EheimDigitalDevice
from eheimdigital.heater import EheimDigitalHeater
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, PRECISION_HALVES as PRECISION_HALVES, PRECISION_TENTHS as PRECISION_TENTHS, PRECISION_WHOLE as PRECISION_WHOLE, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Generic, TypeVar, override

PARALLEL_UPDATES: int
_DeviceT_co = TypeVar('_DeviceT_co', bound=EheimDigitalDevice, covariant=True)

@dataclass(frozen=True, kw_only=True)
class EheimDigitalNumberDescription(NumberEntityDescription, Generic[_DeviceT_co]):
    value_fn: Callable[[_DeviceT_co], float | None]
    set_value_fn: Callable[[_DeviceT_co, float], Awaitable[None]]
    uom_fn: Callable[[_DeviceT_co], str] | None = ...

CLASSICVARIO_DESCRIPTIONS: tuple[EheimDigitalNumberDescription[EheimDigitalClassicVario], ...]
HEATER_DESCRIPTIONS: tuple[EheimDigitalNumberDescription[EheimDigitalHeater], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalNumber(EheimDigitalEntity[_DeviceT_co], NumberEntity, Generic[_DeviceT_co]):
    entity_description: EheimDigitalNumberDescription[_DeviceT_co]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT_co, description: EheimDigitalNumberDescription[_DeviceT_co]) -> None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
