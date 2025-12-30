from . import SqueezeboxConfigEntry as SqueezeboxConfigEntry
from .const import PLAYER_SENSOR_NEXT_ALARM as PLAYER_SENSOR_NEXT_ALARM, SIGNAL_PLAYER_DISCOVERED as SIGNAL_PLAYER_DISCOVERED, STATUS_SENSOR_INFO_TOTAL_ALBUMS as STATUS_SENSOR_INFO_TOTAL_ALBUMS, STATUS_SENSOR_INFO_TOTAL_ARTISTS as STATUS_SENSOR_INFO_TOTAL_ARTISTS, STATUS_SENSOR_INFO_TOTAL_DURATION as STATUS_SENSOR_INFO_TOTAL_DURATION, STATUS_SENSOR_INFO_TOTAL_GENRES as STATUS_SENSOR_INFO_TOTAL_GENRES, STATUS_SENSOR_INFO_TOTAL_SONGS as STATUS_SENSOR_INFO_TOTAL_SONGS, STATUS_SENSOR_LASTSCAN as STATUS_SENSOR_LASTSCAN, STATUS_SENSOR_OTHER_PLAYER_COUNT as STATUS_SENSOR_OTHER_PLAYER_COUNT, STATUS_SENSOR_PLAYER_COUNT as STATUS_SENSOR_PLAYER_COUNT
from .entity import LMSStatusEntity as LMSStatusEntity, SqueezeBoxPlayerUpdateCoordinator as SqueezeBoxPlayerUpdateCoordinator, SqueezeboxEntity as SqueezeboxEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

PARALLEL_UPDATES: int
SERVER_STATUS_SENSORS: tuple[SensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class PlayerSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[SqueezeboxSensorEntity], datetime | None]

PLAYER_SENSORS: tuple[PlayerSensorEntityDescription, ...]
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SqueezeboxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ServerStatusSensor(LMSStatusEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...

class SqueezeboxSensorEntity(SqueezeboxEntity, SensorEntity):
    entity_description: PlayerSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: SqueezeBoxPlayerUpdateCoordinator, description: PlayerSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | None: ...
