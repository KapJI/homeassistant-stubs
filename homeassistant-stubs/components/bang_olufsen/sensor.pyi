from . import BeoConfigEntry as BeoConfigEntry
from .const import CONNECTION_STATUS as CONNECTION_STATUS, DOMAIN as DOMAIN, WebsocketNotification as WebsocketNotification
from .entity import BeoEntity as BeoEntity
from .util import get_remotes as get_remotes, supports_battery as supports_battery
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from mozart_api.models import BatteryState as BatteryState, PairedRemote as PairedRemote

SCAN_INTERVAL: Incomplete
PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: BeoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class BeoSensor(SensorEntity, BeoEntity):
    def __init__(self, config_entry: BeoConfigEntry) -> None: ...

class BeoSensorBatteryLevel(BeoSensor):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, config_entry: BeoConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    async def _update_battery(self, data: BatteryState) -> None: ...

class BeoSensorRemoteBatteryLevel(BeoSensor):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement = PERCENTAGE
    _attr_should_poll: bool
    _attr_state_class: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_native_value: Incomplete
    _remote: Incomplete
    def __init__(self, config_entry: BeoConfigEntry, remote: PairedRemote) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
