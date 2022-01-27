from .const import ATTR_SENSOR_ID as ATTR_SENSOR_ID, CONF_SENSOR_ID as CONF_SENSOR_ID, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CONCENTRATION_MICROGRAMS_PER_CUBIC_METER as CONCENTRATION_MICROGRAMS_PER_CUBIC_METER, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, PERCENTAGE as PERCENTAGE, PRESSURE_PA as PRESSURE_PA, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SensorCommunitySensor(CoordinatorEntity, SensorEntity):
    _attr_attribution: str
    _attr_should_poll: bool
    entity_description: Any
    _attr_unique_id: Any
    _attr_extra_state_attributes: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, description: SensorEntityDescription, sensor_id: int, show_on_map: bool) -> None: ...
    @property
    def native_value(self) -> Union[float, None]: ...
