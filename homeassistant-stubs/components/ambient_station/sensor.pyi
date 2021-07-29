from . import AmbientStation as AmbientStation, AmbientWeatherEntity as AmbientWeatherEntity, SENSOR_TYPES as SENSOR_TYPES, TYPE_SOLARRADIATION as TYPE_SOLARRADIATION, TYPE_SOLARRADIATION_LX as TYPE_SOLARRADIATION_LX
from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, ATTR_MONITORED_CONDITIONS as ATTR_MONITORED_CONDITIONS, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbientWeatherSensor(AmbientWeatherEntity, SensorEntity):
    _attr_unit_of_measurement: Any
    def __init__(self, ambient: AmbientStation, mac_address: str, station_name: str, sensor_type: str, sensor_name: str, device_class: Union[str, None], unit: Union[str, None]) -> None: ...
    _attr_state: Any
    def update_from_latest_data(self) -> None: ...
