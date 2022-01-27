from .const import CONF_BALANCING_AUTHORITY as CONF_BALANCING_AUTHORITY, CONF_BALANCING_AUTHORITY_ABBREV as CONF_BALANCING_AUTHORITY_ABBREV, CONF_SHOW_ON_MAP as CONF_SHOW_ON_MAP, DOMAIN as DOMAIN
from collections.abc import Mapping
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, MASS_POUNDS as MASS_POUNDS, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

ATTR_BALANCING_AUTHORITY: str
SENSOR_TYPE_REALTIME_EMISSIONS_MOER: str
SENSOR_TYPE_REALTIME_EMISSIONS_PERCENT: str
REALTIME_EMISSIONS_SENSOR_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RealtimeEmissionsSensor(CoordinatorEntity, SensorEntity):
    _attr_name: Any
    _attr_unique_id: Any
    _entry: Any
    entity_description: Any
    def __init__(self, coordinator: DataUpdateCoordinator, entry: ConfigEntry, description: SensorEntityDescription) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[Mapping[str, Any], None]: ...
    @property
    def native_value(self) -> StateType: ...
