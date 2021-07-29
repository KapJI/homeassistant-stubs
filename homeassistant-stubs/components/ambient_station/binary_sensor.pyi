from . import AmbientWeatherEntity as AmbientWeatherEntity, SENSOR_TYPES as SENSOR_TYPES, TYPE_BATT1 as TYPE_BATT1, TYPE_BATT10 as TYPE_BATT10, TYPE_BATT2 as TYPE_BATT2, TYPE_BATT3 as TYPE_BATT3, TYPE_BATT4 as TYPE_BATT4, TYPE_BATT5 as TYPE_BATT5, TYPE_BATT6 as TYPE_BATT6, TYPE_BATT7 as TYPE_BATT7, TYPE_BATT8 as TYPE_BATT8, TYPE_BATT9 as TYPE_BATT9, TYPE_BATTOUT as TYPE_BATTOUT, TYPE_BATT_CO2 as TYPE_BATT_CO2, TYPE_PM25IN_BATT as TYPE_PM25IN_BATT, TYPE_PM25_BATT as TYPE_PM25_BATT
from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, ATTR_MONITORED_CONDITIONS as ATTR_MONITORED_CONDITIONS, DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbientWeatherBinarySensor(AmbientWeatherEntity, BinarySensorEntity):
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...
