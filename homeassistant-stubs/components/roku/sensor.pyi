from .const import DOMAIN as DOMAIN
from .coordinator import RokuDataUpdateCoordinator as RokuDataUpdateCoordinator
from .entity import RokuEntity as RokuEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from rokuecp.models import Device as RokuDevice

@dataclass(frozen=True, kw_only=True)
class RokuSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[RokuDevice], str | None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSORS: tuple[RokuSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RokuSensorEntity(RokuEntity, SensorEntity):
    entity_description: RokuSensorEntityDescription
    @property
    def native_value(self) -> str | None: ...
