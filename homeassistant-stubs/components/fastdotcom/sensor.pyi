from . import DATA_UPDATED as DATA_UPDATED
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class SpeedtestSensor(RestoreEntity, SensorEntity):
    _attr_name: str
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_icon: str
    _attr_should_poll: bool
    _speedtest_data: Incomplete
    def __init__(self, speedtest_data: dict[str, Any]) -> None: ...
    _attr_native_value: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def update(self) -> None: ...
    def _schedule_immediate_update(self) -> None: ...
