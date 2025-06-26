from .coordinator import EheimDigitalConfigEntry as EheimDigitalConfigEntry, EheimDigitalUpdateCoordinator as EheimDigitalUpdateCoordinator
from .entity import EheimDigitalEntity as EheimDigitalEntity, exception_handler as exception_handler
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
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class EheimDigitalNumberDescription[_DeviceT: EheimDigitalDevice](NumberEntityDescription):
    value_fn: Callable[[_DeviceT], float | None]
    set_value_fn: Callable[[_DeviceT, float], Awaitable[None]]
    uom_fn: Callable[[_DeviceT], str] | None = ...

CLASSICVARIO_DESCRIPTIONS: tuple[EheimDigitalNumberDescription[EheimDigitalClassicVario], ...]
HEATER_DESCRIPTIONS: tuple[EheimDigitalNumberDescription[EheimDigitalHeater], ...]
GENERAL_DESCRIPTIONS: tuple[EheimDigitalNumberDescription[EheimDigitalDevice], ...]

async def async_setup_entry(hass: HomeAssistant, entry: EheimDigitalConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class EheimDigitalNumber[_DeviceT: EheimDigitalDevice](EheimDigitalEntity[_DeviceT], NumberEntity):
    entity_description: EheimDigitalNumberDescription[_DeviceT]
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: EheimDigitalUpdateCoordinator, device: _DeviceT, description: EheimDigitalNumberDescription[_DeviceT]) -> None: ...
    @override
    @exception_handler
    async def async_set_native_value(self, value: float) -> None: ...
    _attr_native_value: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    @override
    def _async_update_attrs(self) -> None: ...
