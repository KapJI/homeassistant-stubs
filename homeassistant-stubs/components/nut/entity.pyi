from . import PyNUTData as PyNUTData
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SERIAL_NUMBER as ATTR_SERIAL_NUMBER, ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

NUT_DEV_INFO_TO_DEV_INFO: dict[str, str]

class NUTBaseEntity(CoordinatorEntity[DataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    pynut_data: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, entity_description: EntityDescription, data: PyNUTData, unique_id: str) -> None: ...

def _get_nut_device_info(data: PyNUTData) -> DeviceInfo: ...
