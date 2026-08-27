from . import FroniusConfigEntry as FroniusConfigEntry
from .coordinator import FroniusModbusSettingsUpdateCoordinator as FroniusModbusSettingsUpdateCoordinator
from .entity import FroniusEntity as FroniusEntity, FroniusEntityDescription as FroniusEntityDescription, ModbusComponentFn as ModbusComponentFn
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final, override

PARALLEL_UPDATES: Final[int]

@dataclass(frozen=True, kw_only=True)
class FroniusSwitchEntityDescription(FroniusEntityDescription, SwitchEntityDescription):
    component_fn: ModbusComponentFn
    field: str

MODBUS_SWITCH_ENTITY_DESCRIPTIONS: list[FroniusSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: FroniusConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ModbusControlSwitch(FroniusEntity, SwitchEntity):
    entity_description: FroniusSwitchEntityDescription
    coordinator: FroniusModbusSettingsUpdateCoordinator
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FroniusModbusSettingsUpdateCoordinator, description: FroniusSwitchEntityDescription, solar_net_id: str) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_write(self, value: bool) -> None: ...
