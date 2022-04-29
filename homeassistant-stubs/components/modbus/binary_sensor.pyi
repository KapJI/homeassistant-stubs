from . import get_hub as get_hub
from .base_platform import BasePlatform as BasePlatform
from .const import CONF_SLAVE_COUNT as CONF_SLAVE_COUNT
from .modbus import ModbusHub as ModbusHub
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

_LOGGER: Incomplete
PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ModbusBinarySensor(BasePlatform, RestoreEntity, BinarySensorEntity):
    _count: Incomplete
    _coordinator: Incomplete
    _result: Incomplete
    def __init__(self, hub: ModbusHub, entry: dict[str, Any], slave_count: int) -> None: ...
    async def async_setup_slaves(self, hass: HomeAssistant, slave_count: int, entry: dict[str, Any]) -> list[SlaveSensor]: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    _call_active: bool
    _lazy_errors: Incomplete
    _attr_available: bool
    async def async_update(self, now: Union[datetime, None] = ...) -> None: ...

class SlaveSensor(CoordinatorEntity, RestoreEntity, BinarySensorEntity):
    _attr_name: Incomplete
    _attr_device_class: Incomplete
    _attr_available: bool
    _result_inx: Incomplete
    _result_bit: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[Any], idx: int, entry: dict[str, Any]) -> None: ...
    _attr_is_on: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
