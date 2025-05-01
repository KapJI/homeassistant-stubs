from . import BoschAlarmConfigEntry as BoschAlarmConfigEntry
from .entity import BoschAlarmAreaEntity as BoschAlarmAreaEntity
from _typeshed import Incomplete
from bosch_alarm_mode2 import Panel as Panel
from bosch_alarm_mode2.panel import Area as Area
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

@dataclass(kw_only=True, frozen=True)
class BoschAlarmSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[Area], int]
    observe_alarms: bool = ...
    observe_ready: bool = ...
    observe_status: bool = ...

SENSOR_TYPES: list[BoschAlarmSensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: BoschAlarmConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

PARALLEL_UPDATES: int

class BoschAreaSensor(BoschAlarmAreaEntity, SensorEntity):
    entity_description: BoschAlarmSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, panel: Panel, area_id: int, unique_id: str, entity_description: BoschAlarmSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int: ...
