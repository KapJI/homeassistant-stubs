from .base_class import TradfriBaseEntity as TradfriBaseEntity
from .const import ATTR_FILTER_LIFE_REMAINING as ATTR_FILTER_LIFE_REMAINING, CONF_GATEWAY_ID as CONF_GATEWAY_ID, COORDINATOR as COORDINATOR, COORDINATOR_LIST as COORDINATOR_LIST, DOMAIN as DOMAIN, KEY_API as KEY_API
from .coordinator import TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, PERCENTAGE as PERCENTAGE, Platform as Platform, TIME_HOURS as TIME_HOURS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytradfri.command import Command as Command
from pytradfri.device import Device as Device
from typing import Any

_LOGGER: Any

class TradfriSensorEntityDescriptionMixin:
    value: Callable[[Device], Union[Any, None]]
    def __init__(self, value) -> None: ...

class TradfriSensorEntityDescription(SensorEntityDescription, TradfriSensorEntityDescriptionMixin):
    def __init__(self, value, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

def _get_air_quality(device: Device) -> Union[int, None]: ...
def _get_filter_time_left(device: Device) -> int: ...

SENSOR_DESCRIPTIONS_BATTERY: tuple[TradfriSensorEntityDescription, ...]
SENSOR_DESCRIPTIONS_FAN: tuple[TradfriSensorEntityDescription, ...]

def _migrate_old_unique_ids(hass: HomeAssistant, old_unique_id: str, key: str) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TradfriSensor(TradfriBaseEntity, SensorEntity):
    entity_description: TradfriSensorEntityDescription
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: Callable[[Union[Command, list[Command]]], Any], gateway_id: str, description: TradfriSensorEntityDescription) -> None: ...
    _attr_native_value: Any
    def _refresh(self) -> None: ...
