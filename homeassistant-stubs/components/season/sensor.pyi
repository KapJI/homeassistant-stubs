from .const import DOMAIN as DOMAIN, TYPE_ASTRONOMICAL as TYPE_ASTRONOMICAL
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

EQUATOR: str
NORTHERN: str
SOUTHERN: str
STATE_AUTUMN: str
STATE_SPRING: str
STATE_SUMMER: str
STATE_WINTER: str
HEMISPHERE_SEASON_SWAP: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def get_season(current_datetime: datetime, hemisphere: str, season_tracking_type: str) -> str | None: ...

class SeasonSensorEntity(SensorEntity):
    _attr_device_class: Incomplete
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    hemisphere: Incomplete
    type: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry, hemisphere: str) -> None: ...
    _attr_native_value: Incomplete
    def update(self) -> None: ...
