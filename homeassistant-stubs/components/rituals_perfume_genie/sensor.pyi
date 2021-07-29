from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from .entity import DiffuserEntity as DiffuserEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_SIGNAL_STRENGTH as DEVICE_CLASS_SIGNAL_STRENGTH, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

BATTERY_SUFFIX: str
PERFUME_SUFFIX: str
FILL_SUFFIX: str
WIFI_SUFFIX: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiffuserPerfumeSensor(DiffuserEntity):
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def state(self) -> str: ...

class DiffuserFillSensor(DiffuserEntity):
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def icon(self) -> str: ...
    @property
    def state(self) -> str: ...

class DiffuserBatterySensor(DiffuserEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def state(self) -> int: ...

class DiffuserWifiSensor(DiffuserEntity):
    _attr_device_class: Any
    _attr_unit_of_measurement: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def state(self) -> int: ...
