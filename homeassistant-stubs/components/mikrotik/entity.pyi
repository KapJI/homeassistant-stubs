from .const import DOMAIN as DOMAIN
from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry, MikrotikDataUpdateCoordinator as MikrotikDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify

class MikrotikBaseEntity(CoordinatorEntity[MikrotikDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _serial: Incomplete
    def __init__(self, coordinator: MikrotikDataUpdateCoordinator, description: EntityDescription) -> None: ...
    def _base_device_info(self) -> dr.DeviceInfo: ...

class MikrotikEntity(MikrotikBaseEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MikrotikDataUpdateCoordinator, description: EntityDescription) -> None: ...

class MikrotikDeviceEntity(MikrotikBaseEntity):
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _interface: Incomplete
    def __init__(self, config_entry: MikrotikConfigEntry, coordinator: MikrotikDataUpdateCoordinator, description: EntityDescription, interface: dict) -> None: ...
