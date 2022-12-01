from . import EsphomeEntity as EsphomeEntity, EsphomeEnumMapper as EsphomeEnumMapper, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import SensorInfo, SensorState, SensorStateClass as EsphomeSensorStateClass, TextSensorInfo, TextSensorState
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import dt as dt

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_STATE_CLASSES: EsphomeEnumMapper[EsphomeSensorStateClass, Union[SensorStateClass, None]]

class EsphomeSensor(EsphomeEntity[SensorInfo, SensorState], SensorEntity):
    @property
    def force_update(self) -> bool: ...
    @property
    def native_value(self) -> Union[datetime, str, None]: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[SensorDeviceClass, None]: ...
    @property
    def state_class(self) -> Union[SensorStateClass, None]: ...

class EsphomeTextSensor(EsphomeEntity[TextSensorInfo, TextSensorState], SensorEntity):
    @property
    def native_value(self) -> Union[str, None]: ...
