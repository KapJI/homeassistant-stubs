from .entity import EsphomeEntity as EsphomeEntity, platform_async_setup_entry as platform_async_setup_entry
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, SensorInfo, SensorState, SensorStateClass as EsphomeSensorStateClass, TextSensorInfo, TextSensorState
from datetime import date, datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.enum import try_parse_enum as try_parse_enum

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

_STATE_CLASSES: EsphomeEnumMapper[EsphomeSensorStateClass, SensorStateClass | None]

class EsphomeSensor(EsphomeEntity[SensorInfo, SensorState], SensorEntity):
    _attr_force_update: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_suggested_display_precision: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def native_value(self) -> datetime | int | float | None: ...

class EsphomeTextSensor(EsphomeEntity[TextSensorInfo, TextSensorState], SensorEntity):
    _attr_device_class: Incomplete
    @callback
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def native_value(self) -> str | datetime | date | None: ...
