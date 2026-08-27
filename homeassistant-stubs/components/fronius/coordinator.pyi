import abc
from . import FroniusConfigEntry as FroniusConfigEntry, FroniusSolarNet as FroniusSolarNet
from .binary_sensor import POWER_FLOW_BINARY_SENSOR_DESCRIPTIONS as POWER_FLOW_BINARY_SENSOR_DESCRIPTIONS
from .const import DOMAIN as DOMAIN, FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_ID_POWER_FLOW as SOLAR_NET_ID_POWER_FLOW, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM, SolarNetId as SolarNetId
from .entity import FroniusEntity as FroniusEntity, FroniusEntityDescription as FroniusEntityDescription, ModbusComponentFn as ModbusComponentFn
from .number import MODBUS_NUMBER_ENTITY_DESCRIPTIONS as MODBUS_NUMBER_ENTITY_DESCRIPTIONS
from .sensor import INVERTER_ENTITY_DESCRIPTIONS as INVERTER_ENTITY_DESCRIPTIONS, LOGGER_ENTITY_DESCRIPTIONS as LOGGER_ENTITY_DESCRIPTIONS, METER_ENTITY_DESCRIPTIONS as METER_ENTITY_DESCRIPTIONS, MODBUS_INVERTER_ENTITY_DESCRIPTIONS as MODBUS_INVERTER_ENTITY_DESCRIPTIONS, OHMPILOT_ENTITY_DESCRIPTIONS as OHMPILOT_ENTITY_DESCRIPTIONS, POWER_FLOW_ENTITY_DESCRIPTIONS as POWER_FLOW_ENTITY_DESCRIPTIONS, STORAGE_ENTITY_DESCRIPTIONS as STORAGE_ENTITY_DESCRIPTIONS
from .switch import MODBUS_SWITCH_ENTITY_DESCRIPTIONS as MODBUS_SWITCH_ENTITY_DESCRIPTIONS
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from datetime import timedelta
from fronius_modbus import FroniusModbusInverter as FroniusModbusInverter, Mppt as Mppt
from homeassistant.const import Platform as Platform
from homeassistant.core import callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator, UpdateFailed as UpdateFailed
from typing import Any, override

class FroniusCoordinatorBase(ABC, DataUpdateCoordinator[dict[SolarNetId, dict[str, Any]]], metaclass=abc.ABCMeta):
    config_entry: FroniusConfigEntry
    default_interval: timedelta
    error_interval: timedelta
    valid_descriptions: Mapping[Platform, Sequence[FroniusEntityDescription]]
    update_exceptions: tuple[type[Exception], ...]
    MAX_FAILED_UPDATES: int
    _failed_update_count: int
    solar_net: Incomplete
    unregistered_descriptors: dict[SolarNetId, dict[Platform, list[FroniusEntityDescription]]]
    def __init__(self, *args: Any, solar_net: FroniusSolarNet, **kwargs: Any) -> None: ...
    @abstractmethod
    async def _update_method(self) -> dict[SolarNetId, Any]: ...
    @override
    async def _async_update_data(self) -> dict[SolarNetId, Any]: ...
    update_interval: Incomplete
    async def _do_update(self) -> dict[SolarNetId, Any]: ...
    @callback
    def add_entities_for_seen_keys[_FroniusEntityT: FroniusEntity](self, async_add_entities: AddEntitiesCallback, platform: Platform, entity_constructor: type[_FroniusEntityT]) -> None: ...

class FroniusInverterUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions: Incomplete
    SILENT_RETRIES: int
    inverter_info: Incomplete
    def __init__(self, *args: Any, inverter_info: FroniusDeviceInfo, **kwargs: Any) -> None: ...
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusModbusCoordinatorBase(FroniusCoordinatorBase, metaclass=abc.ABCMeta):
    error_interval: Incomplete
    update_exceptions: Incomplete
    inverter_info: Incomplete
    modbus_inverter: Incomplete
    def __init__(self, *args: Any, inverter_info: FroniusDeviceInfo, modbus_inverter: FroniusModbusInverter, **kwargs: Any) -> None: ...
    @override
    async def _async_update_data(self) -> dict[SolarNetId, Any]: ...
    @abstractmethod
    async def _refresh_components(self) -> None: ...
    async def _refresh(self) -> None: ...
    def _as_device_data(self, values: Mapping[str, float | bool | None]) -> dict[SolarNetId, Any]: ...

class FroniusModbusInverterUpdateCoordinator(FroniusModbusCoordinatorBase):
    default_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _refresh_components(self) -> None: ...
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusModbusSettingsUpdateCoordinator(FroniusModbusCoordinatorBase):
    default_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _refresh_components(self) -> None: ...
    async def async_write(self, component_fn: ModbusComponentFn, field: str, value: float | bool, *, enable_field: str | None = None) -> None: ...
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusLoggerUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusMeterUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusOhmpilotUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusPowerFlowUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...

class FroniusStorageUpdateCoordinator(FroniusCoordinatorBase):
    default_interval: Incomplete
    error_interval: Incomplete
    valid_descriptions: Incomplete
    @override
    async def _update_method(self) -> dict[SolarNetId, Any]: ...
