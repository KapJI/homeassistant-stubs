from .const import ATTR_EXPIRES as ATTR_EXPIRES, ATTR_NAME_SERVERS as ATTR_NAME_SERVERS, ATTR_REGISTRAR as ATTR_REGISTRAR, ATTR_UPDATED as ATTR_UPDATED, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from whois import Domain

@dataclass
class WhoisSensorEntityDescriptionMixin:
    value_fn: Callable[[Domain], datetime | int | str | None]
    def __init__(self, value_fn) -> None: ...

@dataclass
class WhoisSensorEntityDescription(SensorEntityDescription, WhoisSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

def _days_until_expiration(domain: Domain) -> int | None: ...
def _ensure_timezone(timestamp: datetime | None) -> datetime | None: ...

SENSORS: tuple[WhoisSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WhoisSensorEntity(CoordinatorEntity[DataUpdateCoordinator[Domain | None]], SensorEntity):
    entity_description: WhoisSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _domain: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[Domain | None], description: WhoisSensorEntityDescription, domain: str) -> None: ...
    @property
    def native_value(self) -> datetime | int | str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, int | float | None] | None: ...
