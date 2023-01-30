from .entity import KaleidescapeEntity as KaleidescapeEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from kaleidescape import Device as KaleidescapeDevice

class BaseEntityDescriptionMixin:
    value_fn: Callable[[KaleidescapeDevice], StateType]
    def __init__(self, value_fn) -> None: ...

class KaleidescapeSensorEntityDescription(SensorEntityDescription, BaseEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_precision, native_unit_of_measurement, options, state_class, suggested_unit_of_measurement) -> None: ...

SENSOR_TYPES: tuple[KaleidescapeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KaleidescapeSensor(KaleidescapeEntity, SensorEntity):
    entity_description: KaleidescapeSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, device: KaleidescapeDevice, entity_description: KaleidescapeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
