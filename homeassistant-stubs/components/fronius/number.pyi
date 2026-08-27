from . import FroniusConfigEntry as FroniusConfigEntry
from .coordinator import FroniusModbusSettingsUpdateCoordinator as FroniusModbusSettingsUpdateCoordinator
from .entity import FroniusEntity as FroniusEntity, FroniusEntityDescription as FroniusEntityDescription, ModbusComponentFn as ModbusComponentFn
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.number import NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: Final[int]

@dataclass(frozen=True, kw_only=True)
class FroniusNumberEntityDescription(FroniusEntityDescription, NumberEntityDescription):
    component_fn: ModbusComponentFn
    field: str
    enable_field: str | None = ...

MODBUS_NUMBER_ENTITY_DESCRIPTIONS: list[FroniusNumberEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: FroniusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ModbusSetpointNumber(FroniusEntity, NumberEntity):
    entity_description: FroniusNumberEntityDescription
    coordinator: FroniusModbusSettingsUpdateCoordinator
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusModbusSettingsUpdateCoordinator, description: FroniusNumberEntityDescription, solar_net_id: str) -> None: ...
    @property
    @override
    def native_value(self) -> float | None: ...
    @override
    async def async_set_native_value(self, value: float) -> None: ...
