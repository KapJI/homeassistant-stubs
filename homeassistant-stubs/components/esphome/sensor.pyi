from . import EsphomeEntity as EsphomeEntity, EsphomeEnumMapper as EsphomeEnumMapper, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import SensorInfo, SensorState, SensorStateClass, TextSensorInfo, TextSensorState
from homeassistant.components.sensor import DEVICE_CLASSES as DEVICE_CLASSES, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import dt as dt
from typing import Any

ICON_SCHEMA: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_STATE_CLASSES: EsphomeEnumMapper[SensorStateClass, Union[str, None]]

class EsphomeSensor(EsphomeEntity[SensorInfo, SensorState], SensorEntity):
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def force_update(self) -> bool: ...
    def native_value(self) -> Union[str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def state_class(self) -> Union[str, None]: ...

class EsphomeTextSensor(EsphomeEntity[TextSensorInfo, TextSensorState], SensorEntity):
    @property
    def icon(self) -> str: ...
    def native_value(self) -> Union[str, None]: ...
