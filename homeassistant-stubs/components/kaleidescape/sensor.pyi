from .entity import KaleidescapeEntity as KaleidescapeEntity
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from kaleidescape import Device as KaleidescapeDevice
from typing import Any

class BaseEntityDescriptionMixin:
    value_fn: Callable[[KaleidescapeDevice], StateType]
    def __init__(self, value_fn) -> None: ...

class KaleidescapeSensorEntityDescription(SensorEntityDescription, BaseEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSOR_TYPES: tuple[KaleidescapeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class KaleidescapeSensor(KaleidescapeEntity, SensorEntity):
    entity_description: KaleidescapeSensorEntityDescription
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, device: KaleidescapeDevice, entity_description: KaleidescapeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
