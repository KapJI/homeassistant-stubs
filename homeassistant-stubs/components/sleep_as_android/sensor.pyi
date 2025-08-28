from . import SleepAsAndroidConfigEntry as SleepAsAndroidConfigEntry
from .const import ALARM_LABEL_DEFAULT as ALARM_LABEL_DEFAULT, ATTR_EVENT as ATTR_EVENT, ATTR_VALUE1 as ATTR_VALUE1, ATTR_VALUE2 as ATTR_VALUE2
from .entity import SleepAsAndroidEntity as SleepAsAndroidEntity
from _typeshed import Incomplete
from enum import StrEnum
from homeassistant.components.sensor import RestoreSensor as RestoreSensor, SensorDeviceClass as SensorDeviceClass, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class SleepAsAndroidSensor(StrEnum):
    NEXT_ALARM = 'next_alarm'
    ALARM_LABEL = 'alarm_label'

SENSOR_DESCRIPTIONS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: SleepAsAndroidConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SleepAsAndroidSensorEntity(SleepAsAndroidEntity, RestoreSensor):
    entity_description: SensorEntityDescription
    _attr_native_value: Incomplete
    @callback
    def _async_handle_event(self, webhook_id: str, data: dict[str, str]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
