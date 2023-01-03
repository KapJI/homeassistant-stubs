from . import PyNUTData as PyNUTData
from .const import COORDINATOR as COORDINATOR, DOMAIN as DOMAIN, KEY_STATUS as KEY_STATUS, KEY_STATUS_DISPLAY as KEY_STATUS_DISPLAY, PYNUT_DATA as PYNUT_DATA, PYNUT_UNIQUE_ID as PYNUT_UNIQUE_ID, SENSOR_TYPES as SENSOR_TYPES, STATE_TYPES as STATE_TYPES
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_MANUFACTURER as ATTR_MANUFACTURER, ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

NUT_DEV_INFO_TO_DEV_INFO: dict[str, str]
_LOGGER: Incomplete

def _get_nut_device_info(data: PyNUTData) -> DeviceInfo: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NUTSensor(CoordinatorEntity[DataUpdateCoordinator[dict[str, str]]], SensorEntity):
    entity_description: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[str, str]], sensor_description: SensorEntityDescription, data: PyNUTData, unique_id: str) -> None: ...
    @property
    def native_value(self) -> Union[str, None]: ...

def _format_display_state(status: dict[str, str]) -> str: ...
