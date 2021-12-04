from .const import CATEGORY_CDC_REPORT as CATEGORY_CDC_REPORT, CATEGORY_USER_REPORT as CATEGORY_USER_REPORT, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_STATE as ATTR_STATE, CONF_LATITUDE as CONF_LATITUDE, CONF_LONGITUDE as CONF_LONGITUDE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_CITY: str
ATTR_REPORTED_DATE: str
ATTR_REPORTED_LATITUDE: str
ATTR_REPORTED_LONGITUDE: str
ATTR_STATE_REPORTS_LAST_WEEK: str
ATTR_STATE_REPORTS_THIS_WEEK: str
ATTR_ZIP_CODE: str
SENSOR_TYPE_CDC_LEVEL: str
SENSOR_TYPE_CDC_LEVEL2: str
SENSOR_TYPE_USER_CHICK: str
SENSOR_TYPE_USER_DENGUE: str
SENSOR_TYPE_USER_FLU: str
SENSOR_TYPE_USER_LEPTO: str
SENSOR_TYPE_USER_NO_SYMPTOMS: str
SENSOR_TYPE_USER_SYMPTOMS: str
SENSOR_TYPE_USER_TOTAL: str
CDC_SENSOR_DESCRIPTIONS: Any
USER_SENSOR_DESCRIPTIONS: Any
EXTENDED_SENSOR_TYPE_MAPPING: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluNearYouSensor(CoordinatorEntity, SensorEntity):
    _attr_unique_id: Any
    _entry: Any
    entity_description: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...

class CdcSensor(FluNearYouSensor):
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def native_value(self) -> StateType: ...

class UserSensor(FluNearYouSensor):
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def native_value(self) -> StateType: ...
