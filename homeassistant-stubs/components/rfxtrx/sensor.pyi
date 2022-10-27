from . import DeviceTuple as DeviceTuple, RfxtrxEntity as RfxtrxEntity, async_setup_platform_entry as async_setup_platform_entry, get_rfx_object as get_rfx_object
from .const import ATTR_EVENT as ATTR_EVENT
from RFXtrx import RFXtrxDevice as RFXtrxDevice, RFXtrxEvent as RFXtrxEvent
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import date, datetime
from decimal import Decimal
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEGREE as DEGREE, ELECTRIC_CURRENT_AMPERE as ELECTRIC_CURRENT_AMPERE, ELECTRIC_POTENTIAL_VOLT as ELECTRIC_POTENTIAL_VOLT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LENGTH_MILLIMETERS as LENGTH_MILLIMETERS, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, PRESSURE_HPA as PRESSURE_HPA, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, SPEED_METERS_PER_SECOND as SPEED_METERS_PER_SECOND, TEMP_CELSIUS as TEMP_CELSIUS, UV_INDEX as UV_INDEX, UnitOfVolumetricFlux as UnitOfVolumetricFlux
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import Entity as Entity, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

_LOGGER: Incomplete

def _battery_convert(value: Union[int, None]) -> Union[int, None]: ...
def _rssi_convert(value: Union[int, None]) -> Union[str, None]: ...

class RfxtrxSensorEntityDescription(SensorEntityDescription):
    convert: Callable[[Any], Union[StateType, date, datetime, Decimal]]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, convert) -> None: ...

SENSOR_TYPES: Incomplete
SENSOR_TYPES_DICT: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RfxtrxSensor(RfxtrxEntity, SensorEntity):
    _attr_force_update: bool
    entity_description: RfxtrxSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, device: RFXtrxDevice, device_id: DeviceTuple, entity_description: RfxtrxSensorEntityDescription, event: Union[RFXtrxEvent, None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def native_value(self) -> Union[StateType, date, datetime, Decimal]: ...
    def _handle_event(self, event: RFXtrxEvent, device_id: DeviceTuple) -> None: ...
