from .const import DOMAIN as DOMAIN
from .coordinator import DataGrandLyonTclCoordinator as DataGrandLyonTclCoordinator, DataGrandLyonVelovCoordinator as DataGrandLyonVelovCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

class DataGrandLyonEntity[_CoordinatorT: DataUpdateCoordinator](CoordinatorEntity[_CoordinatorT]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _subentry_id: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _CoordinatorT, subentry: ConfigSubentry, description: EntityDescription, manufacturer: str, model: str) -> None: ...
    @property
    def available(self) -> bool: ...

class DataGrandLyonTclEntity(DataGrandLyonEntity[DataGrandLyonTclCoordinator]):
    def __init__(self, coordinator: DataGrandLyonTclCoordinator, subentry: ConfigSubentry, description: EntityDescription) -> None: ...

class DataGrandLyonVelovEntity(DataGrandLyonEntity[DataGrandLyonVelovCoordinator]):
    def __init__(self, coordinator: DataGrandLyonVelovCoordinator, subentry: ConfigSubentry, description: EntityDescription) -> None: ...
