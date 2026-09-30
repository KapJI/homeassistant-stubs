from .const import DOMAIN as DOMAIN, SUBSYSTEM_INVERTER as SUBSYSTEM_INVERTER, SUBSYSTEM_POWER_CONTROL as SUBSYSTEM_POWER_CONTROL, SUBSYSTEM_SITE_CONTROL as SUBSYSTEM_SITE_CONTROL
from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry, SolarEdgeModbusDataUpdateCoordinator as SolarEdgeModbusDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from solaredged import Battery as Battery, ExportControl, Meter as Meter, PowerControl, SolarEdge as SolarEdge, StorageControl
from typing import override

def inverter_model(model: str | None) -> str | None: ...
def inverter_name(model: str | None) -> str: ...
type ControlComponent = ExportControl | PowerControl | StorageControl
def _control_subsystem(component: ControlComponent) -> str: ...
def attachment_identity(component: Battery | Meter, index: int) -> str: ...
def inverter_device_info(solaredge: SolarEdge, serial_number: str) -> DeviceInfo: ...

class SolarEdgeModbusEntity(CoordinatorEntity[SolarEdgeModbusDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _subsystem: Incomplete
    _serial_number: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, *, entry: SolarEdgeModbusConfigEntry, subsystem: str, description: EntityDescription, key_prefix: str = '') -> None: ...
    @property
    @override
    def available(self) -> bool: ...

class SolarEdgeModbusInverterEntity(SolarEdgeModbusEntity):
    _attr_device_info: Incomplete
    def __init__(self, *, entry: SolarEdgeModbusConfigEntry, description: EntityDescription, subsystem: str = ...) -> None: ...

class SolarEdgeModbusMeterEntity(SolarEdgeModbusEntity):
    _index: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry: SolarEdgeModbusConfigEntry, description: EntityDescription, index: int) -> None: ...

class SolarEdgeModbusBatteryEntity(SolarEdgeModbusEntity):
    _index: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, *, entry: SolarEdgeModbusConfigEntry, description: EntityDescription, index: int) -> None: ...

class SolarEdgeModbusControlEntity[ComponentT: ControlComponent](SolarEdgeModbusInverterEntity):
    _component: Incomplete
    def __init__(self, *, entry: SolarEdgeModbusConfigEntry, description: EntityDescription, component: ComponentT) -> None: ...
