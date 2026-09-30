from .const import DOMAIN as DOMAIN
from .coordinator import SunsynkDataUpdateCoordinator as SunsynkDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from sunsynk.inverter import Inverter as Inverter

def inverter_device_info(inverter: Inverter) -> DeviceInfo: ...

class SunsynkInverterEntity(CoordinatorEntity[SunsynkDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SunsynkDataUpdateCoordinator, description: EntityDescription) -> None: ...

class SunsynkBatteryEntity(CoordinatorEntity[SunsynkDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: SunsynkDataUpdateCoordinator, description: EntityDescription) -> None: ...
