from .const import ATTR_COMMAND_SET as ATTR_COMMAND_SET, ATTR_INFO as ATTR_INFO, ATTR_MARKER_HIGH_LEVEL as ATTR_MARKER_HIGH_LEVEL, ATTR_MARKER_LOW_LEVEL as ATTR_MARKER_LOW_LEVEL, ATTR_MARKER_TYPE as ATTR_MARKER_TYPE, ATTR_SERIAL as ATTR_SERIAL, ATTR_STATE_MESSAGE as ATTR_STATE_MESSAGE, ATTR_STATE_REASON as ATTR_STATE_REASON, ATTR_URI_SUPPORTED as ATTR_URI_SUPPORTED, DOMAIN as DOMAIN
from .coordinator import IPPDataUpdateCoordinator as IPPDataUpdateCoordinator
from .entity import IPPEntity as IPPEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_LOCATION as ATTR_LOCATION, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utcnow as utcnow
from pyipp import Marker as Marker, Printer as Printer
from typing import Any

@dataclass
class IPPSensorEntityDescriptionMixin:
    value_fn: Callable[[Printer], StateType | datetime]
    def __init__(self, value_fn) -> None: ...

@dataclass
class IPPSensorEntityDescription(SensorEntityDescription, IPPSensorEntityDescriptionMixin):
    attributes_fn: Callable[[Printer], dict[Any, StateType]] = ...
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, attributes_fn) -> None: ...

def _get_marker_attributes_fn(marker_index: int, attributes_fn: Callable[[Marker], dict[Any, StateType]]) -> Callable[[Printer], dict[Any, StateType]]: ...
def _get_marker_value_fn(marker_index: int, value_fn: Callable[[Marker], StateType | datetime]) -> Callable[[Printer], StateType | datetime]: ...

PRINTER_SENSORS: tuple[IPPSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class IPPSensor(IPPEntity, SensorEntity):
    entity_description: IPPSensorEntityDescription
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def native_value(self) -> StateType | datetime: ...
