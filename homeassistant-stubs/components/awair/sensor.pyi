from . import AwairDataUpdateCoordinator as AwairDataUpdateCoordinator, AwairResult as AwairResult
from .const import API_DUST as API_DUST, API_PM25 as API_PM25, API_SCORE as API_SCORE, API_TEMP as API_TEMP, API_VOC as API_VOC, ATTRIBUTION as ATTRIBUTION, AwairSensorEntityDescription as AwairSensorEntityDescription, DOMAIN as DOMAIN, DUST_ALIASES as DUST_ALIASES, SENSOR_TYPES as SENSOR_TYPES, SENSOR_TYPES_DUST as SENSOR_TYPES_DUST, SENSOR_TYPE_SCORE as SENSOR_TYPE_SCORE
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CONNECTIONS as ATTR_CONNECTIONS, ATTR_SW_VERSION as ATTR_SW_VERSION
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from python_awair.air_data import AirData as AirData
from python_awair.devices import AwairBaseDevice as AwairBaseDevice

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AwairSensor(CoordinatorEntity[AwairDataUpdateCoordinator], SensorEntity):
    entity_description: AwairSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_attribution: Incomplete
    _device: Incomplete
    def __init__(self, device: AwairBaseDevice, coordinator: AwairDataUpdateCoordinator, description: AwairSensorEntityDescription) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def native_value(self) -> Union[float, None]: ...
    @property
    def extra_state_attributes(self) -> dict: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def _air_data(self) -> Union[AirData, None]: ...
