import datetime
from . import RoborockCoordinators as RoborockCoordinators
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator, RoborockDataUpdateCoordinatorA01 as RoborockDataUpdateCoordinatorA01
from .device import RoborockCoordinatedEntityA01 as RoborockCoordinatedEntityA01, RoborockCoordinatedEntityV1 as RoborockCoordinatedEntityV1
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import AREA_SQUARE_METERS as AREA_SQUARE_METERS, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util import slugify as slugify
from roborock.roborock_message import RoborockDataProtocol, RoborockDyadDataProtocol
from roborock.roborock_typing import DeviceProp as DeviceProp

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescription(SensorEntityDescription):
    value_fn: Callable[[DeviceProp], StateType | datetime.datetime]
    protocol_listener: RoborockDataProtocol | None = ...
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn, protocol_listener) -> None: ...

@dataclass(frozen=True, kw_only=True)
class RoborockSensorDescriptionA01(SensorEntityDescription):
    data_protocol: RoborockDyadDataProtocol
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, data_protocol) -> None: ...

def _dock_error_value_fn(properties: DeviceProp) -> str | None: ...

SENSOR_DESCRIPTIONS: Incomplete
A01_SENSOR_DESCRIPTIONS: list[RoborockSensorDescriptionA01]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockSensorEntity(RoborockCoordinatedEntityV1, SensorEntity):
    entity_description: RoborockSensorDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, description: RoborockSensorDescription) -> None: ...
    @property
    def native_value(self) -> StateType | datetime.datetime: ...

class RoborockSensorEntityA01(RoborockCoordinatedEntityA01, SensorEntity):
    entity_description: RoborockSensorDescriptionA01
    def __init__(self, coordinator: RoborockDataUpdateCoordinatorA01, description: RoborockSensorDescriptionA01) -> None: ...
    @property
    def native_value(self) -> StateType: ...
