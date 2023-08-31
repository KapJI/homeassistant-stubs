from . import NotionEntity as NotionEntity
from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, SENSOR_BATTERY as SENSOR_BATTERY, SENSOR_DOOR as SENSOR_DOOR, SENSOR_GARAGE_DOOR as SENSOR_GARAGE_DOOR, SENSOR_LEAK as SENSOR_LEAK, SENSOR_MISSING as SENSOR_MISSING, SENSOR_SAFE as SENSOR_SAFE, SENSOR_SLIDING as SENSOR_SLIDING, SENSOR_SMOKE_CO as SENSOR_SMOKE_CO, SENSOR_WINDOW_HINGED as SENSOR_WINDOW_HINGED
from .model import NotionEntityDescriptionMixin as NotionEntityDescriptionMixin
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Literal

class NotionBinarySensorDescriptionMixin:
    on_state: Literal['alarm', 'leak', 'low', 'not_missing', 'open']
    def __init__(self, on_state) -> None: ...

class NotionBinarySensorDescription(BinarySensorEntityDescription, NotionBinarySensorDescriptionMixin, NotionEntityDescriptionMixin):
    def __init__(self, listener_kind, on_state, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

BINARY_SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NotionBinarySensor(NotionEntity, BinarySensorEntity):
    entity_description: NotionBinarySensorDescription
    @property
    def is_on(self) -> bool | None: ...
