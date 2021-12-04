from .const import CONF_LICENSE_PLATE as CONF_LICENSE_PLATE, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from datetime import date
from homeassistant.components.sensor import DEVICE_CLASS_DATE as DEVICE_CLASS_DATE, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any
from vehicle import Vehicle as Vehicle

class RDWSensorEntityDescriptionMixin:
    value_fn: Callable[[Vehicle], Union[date, str, float, None]]

class RDWSensorEntityDescription(SensorEntityDescription, RDWSensorEntityDescriptionMixin): ...

SENSORS: tuple[RDWSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RDWSensorEntity(CoordinatorEntity, SensorEntity):
    entity_description: RDWSensorEntityDescription
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: DataUpdateCoordinator, license_plate: str, description: RDWSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[date, str, float, None]: ...
