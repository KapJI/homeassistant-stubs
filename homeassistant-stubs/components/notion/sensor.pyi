from . import NotionEntity as NotionEntity
from .const import DOMAIN as DOMAIN, SENSOR_MOLD as SENSOR_MOLD, SENSOR_TEMPERATURE as SENSOR_TEMPERATURE
from .model import NotionEntityDescriptionMixin as NotionEntityDescriptionMixin
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass
class NotionSensorDescription(SensorEntityDescription, NotionEntityDescriptionMixin):
    def __init__(self, listener_kind, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NotionSensor(NotionEntity, SensorEntity):
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def native_value(self) -> str | None: ...
