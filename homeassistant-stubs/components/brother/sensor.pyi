from . import BrotherDataUpdateCoordinator as BrotherDataUpdateCoordinator
from .const import DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

ATTR_BELT_UNIT_REMAINING_LIFE: str
ATTR_BLACK_DRUM_COUNTER: str
ATTR_BLACK_DRUM_REMAINING_LIFE: str
ATTR_BLACK_DRUM_REMAINING_PAGES: str
ATTR_BLACK_INK_REMAINING: str
ATTR_BLACK_TONER_REMAINING: str
ATTR_BW_COUNTER: str
ATTR_COLOR_COUNTER: str
ATTR_COUNTER: str
ATTR_CYAN_DRUM_COUNTER: str
ATTR_CYAN_DRUM_REMAINING_LIFE: str
ATTR_CYAN_DRUM_REMAINING_PAGES: str
ATTR_CYAN_INK_REMAINING: str
ATTR_CYAN_TONER_REMAINING: str
ATTR_DRUM_COUNTER: str
ATTR_DRUM_REMAINING_LIFE: str
ATTR_DRUM_REMAINING_PAGES: str
ATTR_DUPLEX_COUNTER: str
ATTR_FUSER_REMAINING_LIFE: str
ATTR_LASER_REMAINING_LIFE: str
ATTR_MAGENTA_DRUM_COUNTER: str
ATTR_MAGENTA_DRUM_REMAINING_LIFE: str
ATTR_MAGENTA_DRUM_REMAINING_PAGES: str
ATTR_MAGENTA_INK_REMAINING: str
ATTR_MAGENTA_TONER_REMAINING: str
ATTR_MANUFACTURER: str
ATTR_PAGE_COUNTER: str
ATTR_PF_KIT_1_REMAINING_LIFE: str
ATTR_PF_KIT_MP_REMAINING_LIFE: str
ATTR_REMAINING_PAGES: str
ATTR_STATUS: str
ATTR_UPTIME: str
ATTR_YELLOW_DRUM_COUNTER: str
ATTR_YELLOW_DRUM_REMAINING_LIFE: str
ATTR_YELLOW_DRUM_REMAINING_PAGES: str
ATTR_YELLOW_INK_REMAINING: str
ATTR_YELLOW_TONER_REMAINING: str
UNIT_PAGES: str
ATTRS_MAP: dict[str, tuple[str, str]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class BrotherPrinterSensor(CoordinatorEntity, SensorEntity):
    _attrs: Any
    _attr_device_info: Any
    _attr_name: Any
    _attr_unique_id: Any
    entity_description: Any
    def __init__(self, coordinator: BrotherDataUpdateCoordinator, description: BrotherSensorEntityDescription, device_info: DeviceInfo) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...

class BrotherPrinterUptimeSensor(BrotherPrinterSensor):
    @property
    def native_value(self) -> datetime: ...

class BrotherSensorEntityDescription(SensorEntityDescription):
    entity_class: type[BrotherPrinterSensor]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, entity_class) -> None: ...

SENSOR_TYPES: tuple[BrotherSensorEntityDescription, ...]
