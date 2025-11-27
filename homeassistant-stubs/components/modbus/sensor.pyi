from . import get_hub as get_hub
from .const import CONF_SCALE as CONF_SCALE, CONF_SLAVE_COUNT as CONF_SLAVE_COUNT, CONF_VIRTUAL_COUNT as CONF_VIRTUAL_COUNT, DEFAULT_OFFSET as DEFAULT_OFFSET, DEFAULT_SCALE as DEFAULT_SCALE, _LOGGER as _LOGGER
from .entity import ModbusStructEntity as ModbusStructEntity
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, RestoreSensor as RestoreSensor, SensorEntity as SensorEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, CONF_OFFSET as CONF_OFFSET, CONF_SENSORS as CONF_SENSORS, CONF_UNIQUE_ID as CONF_UNIQUE_ID, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ModbusRegisterSensor(ModbusStructEntity, RestoreSensor, SensorEntity):
    _count: Incomplete
    _coordinator: DataUpdateCoordinator[list[float | None] | None] | None
    _scale: Incomplete
    _offset: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_device_class: Incomplete
    _value_is_int: bool
    _attr_suggested_display_precision: Incomplete
    def __init__(self, hass: HomeAssistant, hub: ModbusHub, entry: dict[str, Any], slave_count: int) -> None: ...
    async def async_setup_slaves(self, hass: HomeAssistant, slave_count: int, entry: dict[str, Any]) -> list[SlaveSensor]: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    _attr_available: bool
    async def _async_update(self) -> None: ...

class SlaveSensor(CoordinatorEntity[DataUpdateCoordinator[list[float | None] | None]], RestoreSensor, SensorEntity):
    @property
    def available(self) -> bool: ...
    _idx: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_device_class: Incomplete
    _attr_available: bool
    def __init__(self, coordinator: DataUpdateCoordinator[list[float | None] | None], idx: int, entry: dict[str, Any]) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _handle_coordinator_update(self) -> None: ...
