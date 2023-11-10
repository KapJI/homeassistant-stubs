from . import DOMAIN as DOMAIN, PrusaLinkEntity as PrusaLinkEntity, PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfLength as UnitOfLength, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.variance import ignore_variance as ignore_variance
from pyprusalink import JobInfo, PrinterInfo
from typing import Generic, TypeVar

T = TypeVar('T', PrinterInfo, JobInfo)

@dataclass
class PrusaLinkSensorEntityDescriptionMixin(Generic[T]):
    value_fn: Callable[[T], datetime | StateType]
    def __init__(self, value_fn) -> None: ...

@dataclass
class PrusaLinkSensorEntityDescription(SensorEntityDescription, PrusaLinkSensorEntityDescriptionMixin[T], Generic[T]):
    available_fn: Callable[[T], bool] = ...
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, available_fn) -> None: ...

SENSORS: dict[str, tuple[PrusaLinkSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrusaLinkSensorEntity(PrusaLinkEntity, SensorEntity):
    entity_description: PrusaLinkSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> datetime | StateType: ...
    @property
    def available(self) -> bool: ...
