from . import AmbientWeatherEntity as AmbientWeatherEntity
from .const import ATTR_LAST_DATA as ATTR_LAST_DATA, DOMAIN as DOMAIN
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_CONNECTIVITY as DEVICE_CLASS_CONNECTIVITY
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_NAME as ATTR_NAME, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Literal

TYPE_BATT1: str
TYPE_BATT10: str
TYPE_BATT2: str
TYPE_BATT3: str
TYPE_BATT4: str
TYPE_BATT5: str
TYPE_BATT6: str
TYPE_BATT7: str
TYPE_BATT8: str
TYPE_BATT9: str
TYPE_BATT_CO2: str
TYPE_BATTOUT: str
TYPE_PM25_BATT: str
TYPE_PM25IN_BATT: str
TYPE_RELAY1: str
TYPE_RELAY10: str
TYPE_RELAY2: str
TYPE_RELAY3: str
TYPE_RELAY4: str
TYPE_RELAY5: str
TYPE_RELAY6: str
TYPE_RELAY7: str
TYPE_RELAY8: str
TYPE_RELAY9: str

class AmbientBinarySensorDescriptionMixin:
    on_state: Literal[0, 1]

class AmbientBinarySensorDescription(BinarySensorEntityDescription, AmbientBinarySensorDescriptionMixin): ...

BINARY_SENSOR_DESCRIPTIONS: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AmbientWeatherBinarySensor(AmbientWeatherEntity, BinarySensorEntity):
    entity_description: AmbientBinarySensorDescription
    _attr_is_on: Any
    def update_from_latest_data(self) -> None: ...
