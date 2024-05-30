from . import TedeeConfigEntry as TedeeConfigEntry
from .entity import TedeeDescriptionEntity as TedeeDescriptionEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pytedee_async import TedeeLock as TedeeLock

@dataclass(frozen=True, kw_only=True)
class TedeeSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[TedeeLock], float | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

ENTITIES: tuple[TedeeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: TedeeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TedeeSensorEntity(TedeeDescriptionEntity, SensorEntity):
    entity_description: TedeeSensorEntityDescription
    @property
    def native_value(self) -> float | None: ...
