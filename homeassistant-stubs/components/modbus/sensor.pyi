from . import get_hub as get_hub
from .base_platform import BaseStructPlatform as BaseStructPlatform
from .modbus import ModbusHub as ModbusHub
from datetime import datetime
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENSORS as CONF_SENSORS, CONF_UNIT_OF_MEASUREMENT as CONF_UNIT_OF_MEASUREMENT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ModbusRegisterSensor(BaseStructPlatform, RestoreEntity, SensorEntity):
    _attr_native_unit_of_measurement: Any
    _attr_state_class: Any
    def __init__(self, hub: ModbusHub, entry: dict[str, Any]) -> None: ...
    _attr_native_value: Any
    async def async_added_to_hass(self) -> None: ...
    _lazy_errors: Any
    _attr_available: bool
    async def async_update(self, now: Union[datetime, None] = ...) -> None: ...
