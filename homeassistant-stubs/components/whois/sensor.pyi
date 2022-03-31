from .const import ATTR_EXPIRES as ATTR_EXPIRES, ATTR_NAME_SERVERS as ATTR_NAME_SERVERS, ATTR_REGISTRAR as ATTR_REGISTRAR, ATTR_UPDATED as ATTR_UPDATED, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_DOMAIN as CONF_DOMAIN, TIME_DAYS as TIME_DAYS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any
from whois import Domain as Domain

class WhoisSensorEntityDescriptionMixin:
    value_fn: Callable[[Domain], Union[datetime, int, str, None]]
    def __init__(self, value_fn) -> None: ...

class WhoisSensorEntityDescription(SensorEntityDescription, WhoisSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

def _days_until_expiration(domain: Domain) -> Union[int, None]: ...
def _ensure_timezone(timestamp: Union[datetime, None]) -> Union[datetime, None]: ...

SENSORS: tuple[WhoisSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WhoisSensorEntity(CoordinatorEntity, SensorEntity):
    entity_description: WhoisSensorEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    _domain: Any
    def __init__(self, coordinator: DataUpdateCoordinator, description: WhoisSensorEntityDescription, domain: str) -> None: ...
    @property
    def native_value(self) -> Union[datetime, int, str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Union[int, float, None]], None]: ...
