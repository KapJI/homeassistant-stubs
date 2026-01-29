from .const import DEVICE_TYPE_TAGS as DEVICE_TYPE_TAGS, DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, MieleAppliance as MieleAppliance, StateStatus as StateStatus
from .coordinator import MieleAuxDataUpdateCoordinator as MieleAuxDataUpdateCoordinator, MieleDataUpdateCoordinator as MieleDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pymiele import MieleAPI as MieleAPI, MieleAction as MieleAction, MieleDevice as MieleDevice, MieleFillingLevel as MieleFillingLevel

class MieleBaseEntity[_MieleCoordinatorT: MieleDataUpdateCoordinator | MieleAuxDataUpdateCoordinator](CoordinatorEntity[_MieleCoordinatorT]):
    _attr_has_entity_name: bool
    @staticmethod
    def get_unique_id(device_id: str, description: EntityDescription) -> str: ...
    _device_id: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: _MieleCoordinatorT, device_id: str, description: EntityDescription) -> None: ...
    @property
    def api(self) -> MieleAPI: ...

class MieleEntity(MieleBaseEntity[MieleDataUpdateCoordinator]):
    _attr_device_info: Incomplete
    def __init__(self, coordinator: MieleDataUpdateCoordinator, device_id: str, description: EntityDescription) -> None: ...
    @property
    def device(self) -> MieleDevice: ...
    @property
    def action(self) -> MieleAction: ...
    @property
    def available(self) -> bool: ...

class MieleAuxEntity(MieleBaseEntity[MieleAuxDataUpdateCoordinator]):
    @property
    def levels(self) -> MieleFillingLevel: ...
