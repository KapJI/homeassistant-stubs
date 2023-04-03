from . import get_hub as get_hub
from .base_platform import BaseStructPlatform as BaseStructPlatform
from .const import CONF_SLAVE_COUNT as CONF_SLAVE_COUNT
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, RestoreSensor as RestoreSensor, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class ModbusRegisterSensor(BaseStructPlatform, RestoreSensor, SensorEntity):
    _coordinator: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    def __init__(self, hub: ModbusHub, entry: dict[str, Any]) -> None: ...
    async def async_setup_slaves(self, hass: HomeAssistant, slave_count: int, entry: dict[str, Any]) -> list[SlaveSensor]: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    _lazy_errors: Incomplete
    _attr_available: bool
    async def async_update(self, now: datetime | None = ...) -> None: ...

class SlaveSensor(CoordinatorEntity[DataUpdateCoordinator[list[int] | None]], RestoreSensor, SensorEntity):
    _idx: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_available: bool
    def __init__(self, coordinator: DataUpdateCoordinator[list[int] | None], idx: int, entry: dict[str, Any]) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
