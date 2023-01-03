from . import DOMAIN as DOMAIN, PrusaLinkEntity as PrusaLinkEntity, PrusaLinkUpdateCoordinator as PrusaLinkUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import PERCENTAGE as PERCENTAGE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from homeassistant.util.variance import ignore_variance as ignore_variance
from pyprusalink import JobInfo, PrinterInfo
from typing import TypeVar

T = TypeVar('T', PrinterInfo, JobInfo)

class PrusaLinkSensorEntityDescriptionMixin:
    value_fn: Callable[[T], Union[datetime, StateType]]
    def __init__(self, value_fn) -> None: ...

class PrusaLinkSensorEntityDescription(SensorEntityDescription, PrusaLinkSensorEntityDescriptionMixin[T]):
    available_fn: Callable[[T], bool]
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, suggested_unit_of_measurement, last_reset, native_unit_of_measurement, state_class, available_fn) -> None: ...

SENSORS: dict[str, tuple[PrusaLinkSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PrusaLinkSensorEntity(PrusaLinkEntity, SensorEntity):
    entity_description: PrusaLinkSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PrusaLinkUpdateCoordinator, description: PrusaLinkSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> Union[datetime, StateType]: ...
    @property
    def available(self) -> bool: ...
