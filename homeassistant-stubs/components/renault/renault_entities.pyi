from .renault_vehicle import RenaultVehicleProxy as RenaultVehicleProxy
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from homeassistant.util import slugify as slugify
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData, KamereonVehicleChargeModeData, KamereonVehicleCockpitData, KamereonVehicleHvacStatusData
from typing import Any, Optional, TypeVar

ATTR_LAST_UPDATE: str
T = TypeVar('T')

class RenaultDataEntity(CoordinatorEntity[Optional[T]], Entity):
    vehicle: Any
    _entity_type: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, vehicle: RenaultVehicleProxy, entity_type: str, coordinator_key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def data(self) -> Union[T, None]: ...

class RenaultBatteryDataEntity(RenaultDataEntity[KamereonVehicleBatteryStatusData]):
    def __init__(self, vehicle: RenaultVehicleProxy, entity_type: str) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def is_charging(self) -> bool: ...
    @property
    def is_plugged_in(self) -> bool: ...

class RenaultChargeModeDataEntity(RenaultDataEntity[KamereonVehicleChargeModeData]):
    def __init__(self, vehicle: RenaultVehicleProxy, entity_type: str) -> None: ...

class RenaultCockpitDataEntity(RenaultDataEntity[KamereonVehicleCockpitData]):
    def __init__(self, vehicle: RenaultVehicleProxy, entity_type: str) -> None: ...

class RenaultHVACDataEntity(RenaultDataEntity[KamereonVehicleHvacStatusData]):
    def __init__(self, vehicle: RenaultVehicleProxy, entity_type: str) -> None: ...
