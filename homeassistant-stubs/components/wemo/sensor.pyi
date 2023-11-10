from . import async_wemo_dispatcher_connect as async_wemo_dispatcher_connect
from .entity import WemoEntity as WemoEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass
class AttributeSensorDescription(SensorEntityDescription):
    name: str | None = ...
    state_conversion: Callable[[StateType], StateType] | None = ...
    unique_id_suffix: str | None = ...
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, state_conversion, unique_id_suffix) -> None: ...

ATTRIBUTE_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, _config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AttributeSensor(WemoEntity, SensorEntity):
    entity_description: AttributeSensorDescription
    def __init__(self, coordinator: DeviceCoordinator, description: AttributeSensorDescription) -> None: ...
    @property
    def name_suffix(self) -> str | None: ...
    @property
    def unique_id_suffix(self) -> str | None: ...
    def convert_state(self, value: StateType) -> StateType: ...
    @property
    def native_value(self) -> StateType: ...
