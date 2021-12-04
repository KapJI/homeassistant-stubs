from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from .entity import DiffuserEntity as DiffuserEntity
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

BATTERY_SUFFIX: str
PERFUME_SUFFIX: str
FILL_SUFFIX: str
WIFI_SUFFIX: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiffuserPerfumeSensor(DiffuserEntity, SensorEntity):
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def native_value(self) -> str: ...

class DiffuserFillSensor(DiffuserEntity, SensorEntity):
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def native_value(self) -> str: ...

class DiffuserBatterySensor(DiffuserEntity, SensorEntity):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_entity_category: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> int: ...

class DiffuserWifiSensor(DiffuserEntity, SensorEntity):
    _attr_device_class: Any
    _attr_native_unit_of_measurement: Any
    _attr_entity_category: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> int: ...
