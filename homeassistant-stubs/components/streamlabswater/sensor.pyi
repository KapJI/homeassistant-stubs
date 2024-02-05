from . import StreamlabsCoordinator as StreamlabsCoordinator
from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsData as StreamlabsData
from .entity import StreamlabsWaterEntity as StreamlabsWaterEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

@dataclass(frozen=True, kw_only=True)
class StreamlabsWaterSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[StreamlabsData], StateType]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement, value_fn) -> None: ...

SENSORS: tuple[StreamlabsWaterSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StreamLabsSensor(StreamlabsWaterEntity, SensorEntity):
    entity_description: StreamlabsWaterSensorEntityDescription
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str, entity_description: StreamlabsWaterSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
