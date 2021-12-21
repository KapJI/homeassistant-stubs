import abc
from . import FroniusSolarNet as FroniusSolarNet
from .const import FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_ID_POWER_FLOW as SOLAR_NET_ID_POWER_FLOW, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM, SolarNetId as SolarNetId
from .sensor import INVERTER_ENTITY_DESCRIPTIONS as INVERTER_ENTITY_DESCRIPTIONS, LOGGER_ENTITY_DESCRIPTIONS as LOGGER_ENTITY_DESCRIPTIONS, METER_ENTITY_DESCRIPTIONS as METER_ENTITY_DESCRIPTIONS, OHMPILOT_ENTITY_DESCRIPTIONS as OHMPILOT_ENTITY_DESCRIPTIONS, POWER_FLOW_ENTITY_DESCRIPTIONS as POWER_FLOW_ENTITY_DESCRIPTIONS, STORAGE_ENTITY_DESCRIPTIONS as STORAGE_ENTITY_DESCRIPTIONS, _FroniusSensorEntity as _FroniusSensorEntity
from abc import ABC, abstractmethod
from datetime import timedelta
from homeassistant.components.sensor import SensorEntityDescription as SensorEntityDescription
from homeassistant.core import callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, Dict, TypeVar

FroniusEntityType = TypeVar('FroniusEntityType', bound=_FroniusSensorEntity)

class FroniusCoordinatorBase(ABC, DataUpdateCoordinator[Dict[SolarNetId, Dict[str, Any]]], metaclass=abc.ABCMeta):
    default_interval: timedelta
    error_interval: timedelta
    valid_descriptions: list[SensorEntityDescription]
    MAX_FAILED_UPDATES: int
    _failed_update_count: int
    solar_net: Any
    unregistered_keys: Any
    def __init__(self, *args: Any, solar_net: FroniusSolarNet, **kwargs: Any) -> None: ...
    @abstractmethod
    async def _update_method(self) -> dict[SolarNetId, Any]: ...
    update_interval: Any
    async def _async_update_data(self) -> dict[SolarNetId, Any]: ...
    def add_entities_for_seen_keys(self, async_add_entities: AddEntitiesCallback, entity_constructor: type[FroniusEntityType]) -> None: ...

class FroniusInverterUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Any
    error_interval: Any
    valid_descriptions: Any
    SILENT_RETRIES: int
    inverter_info: Any
    def __init__(self, *args: Any, inverter_info: FroniusDeviceInfo, **kwargs: Any) -> None: ...
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusLoggerUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Any
    error_interval: Any
    valid_descriptions: Any
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusMeterUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Any
    error_interval: Any
    valid_descriptions: Any
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusOhmpilotUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Any
    error_interval: Any
    valid_descriptions: Any
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusPowerFlowUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Any
    error_interval: Any
    valid_descriptions: Any
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusStorageUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Any
    error_interval: Any
    valid_descriptions: Any
    async def _update_method(self) -> dict[SolarNetId, Any]: ...
