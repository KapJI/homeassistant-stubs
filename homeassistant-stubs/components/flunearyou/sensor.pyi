from .const import CATEGORY_CDC_REPORT as CATEGORY_CDC_REPORT, CATEGORY_USER_REPORT as CATEGORY_USER_REPORT, DATA_COORDINATOR as DATA_COORDINATOR, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION as ATTR_ATTRIBUTION, ATTR_STATE as ATTR_STATE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_CITY: str
ATTR_REPORTED_DATE: str
ATTR_REPORTED_LATITUDE: str
ATTR_REPORTED_LONGITUDE: str
ATTR_STATE_REPORTS_LAST_WEEK: str
ATTR_STATE_REPORTS_THIS_WEEK: str
ATTR_ZIP_CODE: str
DEFAULT_ATTRIBUTION: str
SENSOR_TYPE_CDC_LEVEL: str
SENSOR_TYPE_CDC_LEVEL2: str
SENSOR_TYPE_USER_CHICK: str
SENSOR_TYPE_USER_DENGUE: str
SENSOR_TYPE_USER_FLU: str
SENSOR_TYPE_USER_LEPTO: str
SENSOR_TYPE_USER_NO_SYMPTOMS: str
SENSOR_TYPE_USER_SYMPTOMS: str
SENSOR_TYPE_USER_TOTAL: str
CDC_SENSORS: Any
USER_SENSORS: Any
EXTENDED_SENSOR_TYPE_MAPPING: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluNearYouSensor(CoordinatorEntity, SensorEntity):
    _attr_extra_state_attributes: Any
    _attr_icon: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    _entry: Any
    _sensor_type: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, sensor_type: str, name: str, icon: str, unit: Union[str, None]) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def update_from_latest_data(self) -> None: ...

class CdcSensor(FluNearYouSensor):
    _attr_state: Any
    def update_from_latest_data(self) -> None: ...

class UserSensor(FluNearYouSensor):
    _attr_state: Any
    def update_from_latest_data(self) -> None: ...
