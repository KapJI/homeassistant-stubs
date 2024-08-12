from .const import DOMAIN as DOMAIN
from .coordinator import RAVEnDataCoordinator as RAVEnDataCoordinator
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass, StateType as StateType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_MAC as CONF_MAC, EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

@dataclass(frozen=True, kw_only=True)
class RAVEnSensorEntityDescription(SensorEntityDescription):
    message_key: str
    attribute_keys: list[str] | None = ...
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., last_reset=..., native_unit_of_measurement=..., options=..., state_class=..., suggested_display_precision=..., suggested_unit_of_measurement=..., message_key, attribute_keys=...) -> None: ...

SENSORS: Incomplete
DIAGNOSTICS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RAVEnSensor(CoordinatorEntity[RAVEnDataCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: RAVEnSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RAVEnDataCoordinator, entity_description: RAVEnSensorEntityDescription) -> None: ...
    @property
    def _data(self) -> Any: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    @property
    def native_value(self) -> StateType: ...

class RAVEnMeterSensor(RAVEnSensor):
    _meter_mac_addr: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RAVEnDataCoordinator, entity_description: RAVEnSensorEntityDescription, meter_mac_addr: str) -> None: ...
    @property
    def _data(self) -> Any: ...
