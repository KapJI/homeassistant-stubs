import abc
from .const import DOMAIN as DOMAIN
from .coordinator import TeslemetryEnergyHistoryCoordinator as TeslemetryEnergyHistoryCoordinator, TeslemetryEnergySiteInfoCoordinator as TeslemetryEnergySiteInfoCoordinator, TeslemetryEnergySiteLiveCoordinator as TeslemetryEnergySiteLiveCoordinator, TeslemetryVehicleDataCoordinator as TeslemetryVehicleDataCoordinator
from .models import TeslemetryEnergyData as TeslemetryEnergyData, TeslemetryVehicleData as TeslemetryVehicleData
from _typeshed import Incomplete
from abc import abstractmethod
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from tesla_fleet_api.const import Scope as Scope
from tesla_fleet_api.teslemetry import EnergySite as EnergySite, Vehicle as Vehicle
from typing import Any

class TeslemetryRootEntity(Entity):
    _attr_has_entity_name: bool
    scoped: bool
    def raise_for_scope(self, scope: Scope) -> None: ...

class TeslemetryPollingEntity(TeslemetryRootEntity, CoordinatorEntity[TeslemetryVehicleDataCoordinator | TeslemetryEnergyHistoryCoordinator | TeslemetryEnergySiteLiveCoordinator | TeslemetryEnergySiteInfoCoordinator], metaclass=abc.ABCMeta):
    key: Incomplete
    _attr_translation_key: Incomplete
    def __init__(self, coordinator: TeslemetryVehicleDataCoordinator | TeslemetryEnergyHistoryCoordinator | TeslemetryEnergySiteLiveCoordinator | TeslemetryEnergySiteInfoCoordinator, key: str) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def _value(self) -> Any | None: ...
    def get(self, key: str, default: Any | None = None) -> Any | None: ...
    def get_number(self, key: str, default: float) -> float: ...
    @property
    def is_none(self) -> bool: ...
    def _handle_coordinator_update(self) -> None: ...
    @abstractmethod
    def _async_update_attrs(self) -> None: ...

class TeslemetryVehiclePollingEntity(TeslemetryPollingEntity, metaclass=abc.ABCMeta):
    _last_update: int
    api: Vehicle
    vehicle: TeslemetryVehicleData
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_entity_registry_enabled_default: bool
    def __init__(self, data: TeslemetryVehicleData, key: str) -> None: ...
    @property
    def _value(self) -> Any | None: ...

class TeslemetryEnergyLiveEntity(TeslemetryPollingEntity, metaclass=abc.ABCMeta):
    api: EnergySite
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: TeslemetryEnergyData, key: str) -> None: ...

class TeslemetryEnergyInfoEntity(TeslemetryPollingEntity, metaclass=abc.ABCMeta):
    api: EnergySite
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: TeslemetryEnergyData, key: str) -> None: ...

class TeslemetryEnergyHistoryEntity(TeslemetryPollingEntity, metaclass=abc.ABCMeta):
    api: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: TeslemetryEnergyData, key: str) -> None: ...

class TeslemetryWallConnectorEntity(TeslemetryPollingEntity, metaclass=abc.ABCMeta):
    _attr_has_entity_name: bool
    api: EnergySite
    din: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: TeslemetryEnergyData, din: str, key: str) -> None: ...
    @property
    def _value(self) -> StateType: ...
    @property
    def exists(self) -> bool: ...

class TeslemetryVehicleStreamEntity(TeslemetryRootEntity):
    api: Vehicle
    vehicle: Incomplete
    stream: Incomplete
    vin: Incomplete
    add_field: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, data: TeslemetryVehicleData, key: str) -> None: ...
