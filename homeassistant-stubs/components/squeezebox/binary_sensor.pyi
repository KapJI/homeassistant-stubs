from . import SqueezeBoxPlayerUpdateCoordinator as SqueezeBoxPlayerUpdateCoordinator, SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import PLAYER_SENSOR_ALARM_ACTIVE as PLAYER_SENSOR_ALARM_ACTIVE, PLAYER_SENSOR_ALARM_SNOOZE as PLAYER_SENSOR_ALARM_SNOOZE, PLAYER_SENSOR_ALARM_UPCOMING as PLAYER_SENSOR_ALARM_UPCOMING, SIGNAL_PLAYER_DISCOVERED as SIGNAL_PLAYER_DISCOVERED, STATUS_SENSOR_NEEDSRESTART as STATUS_SENSOR_NEEDSRESTART, STATUS_SENSOR_RESCAN as STATUS_SENSOR_RESCAN
from .entity import LMSStatusEntity as LMSStatusEntity, SqueezeboxEntity as SqueezeboxEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
SERVER_SENSORS: tuple[BinarySensorEntityDescription, ...]
PLAYER_SENSORS: tuple[BinarySensorEntityDescription, ...]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ServerStatusBinarySensor(LMSStatusEntity, BinarySensorEntity):
    @property
    def is_on(self) -> bool: ...

class SqueezeboxBinarySensorEntity(SqueezeboxEntity, BinarySensorEntity):
    description: BinarySensorEntityDescription
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SqueezeBoxPlayerUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
