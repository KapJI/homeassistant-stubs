from .const import OumanDevice as OumanDevice
from .coordinator import OumanEh800ConfigEntry as OumanEh800ConfigEntry, OumanEh800Coordinator as OumanEh800Coordinator
from .entity import OumanEh800Entity as OumanEh800Entity, OumanEh800EntityDescription as OumanEh800EntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription, NumberMode as NumberMode
from homeassistant.const import EntityCategory as EntityCategory, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ouman_eh_800_api import FloatControlOumanEndpoint, IntControlOumanEndpoint
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OumanEh800NumberEntityDescription(OumanEh800EntityDescription, NumberEntityDescription): ...

def _temperature_number(*, device: OumanDevice, key: str, device_class: NumberDeviceClass = ..., entity_category: EntityCategory | None = ..., enabled_by_default: bool = True) -> OumanEh800NumberEntityDescription: ...

NUMBER_DESCRIPTIONS: dict[IntControlOumanEndpoint | FloatControlOumanEndpoint, OumanEh800NumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OumanEh800NumberEntity(OumanEh800Entity, NumberEntity):
    entity_description: OumanEh800NumberEntityDescription
    _endpoint: IntControlOumanEndpoint | FloatControlOumanEndpoint
    _attr_native_min_value: Incomplete
    _attr_native_max_value: Incomplete
    _attr_native_step: Incomplete
    def __init__(self, coordinator: OumanEh800Coordinator, endpoint: IntControlOumanEndpoint | FloatControlOumanEndpoint, description: OumanEh800NumberEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> float: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
