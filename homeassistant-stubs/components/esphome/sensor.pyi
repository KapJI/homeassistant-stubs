from . import EsphomeEntity as EsphomeEntity, EsphomeEnumMapper as EsphomeEnumMapper, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import SensorInfo, SensorState, SensorStateClass, TextSensorInfo, TextSensorState
from homeassistant.components.sensor import DEVICE_CLASSES as DEVICE_CLASSES, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.util import dt as dt
from typing import Any

ICON_SCHEMA: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

_STATE_CLASSES: EsphomeEnumMapper[SensorStateClass, Union[str, None]]

class EsphomeSensor(EsphomeEntity[SensorInfo, SensorState], SensorEntity, RestoreEntity):
    _old_state: Union[float, None]
    _attr_last_reset: Any
    async def async_added_to_hass(self) -> None: ...
    def _on_state_update(self) -> None: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def force_update(self) -> bool: ...
    def state(self) -> Union[str, None]: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def state_class(self) -> Union[str, None]: ...

class EsphomeTextSensor(EsphomeEntity[TextSensorInfo, TextSensorState], SensorEntity):
    @property
    def icon(self) -> str: ...
    def state(self) -> Union[str, None]: ...
