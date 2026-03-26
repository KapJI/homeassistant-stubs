from . import get_device_info as get_device_info
from .const import ATTRIBUTION as ATTRIBUTION, CONDITION_MAP as CONDITION_MAP, DOMAIN as DOMAIN
from .coordinator import MetOfficeConfigEntry as MetOfficeConfigEntry, MetOfficeRuntimeData as MetOfficeRuntimeData, MetOfficeUpdateCoordinator as MetOfficeUpdateCoordinator
from .helpers import get_attribute as get_attribute
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.sensor import EntityCategory as EntityCategory, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import DEGREE as DEGREE, PERCENTAGE as PERCENTAGE, UV_INDEX as UV_INDEX, UnitOfLength as UnitOfLength, UnitOfPressure as UnitOfPressure, UnitOfSpeed as UnitOfSpeed, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

ATTR_LAST_UPDATE: str

@dataclass(frozen=True, kw_only=True)
class MetOfficeSensorEntityDescription(SensorEntityDescription):
    native_attr_name: str

SENSOR_TYPES: tuple[MetOfficeSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: MetOfficeConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MetOfficeCurrentSensor(CoordinatorEntity[MetOfficeUpdateCoordinator], SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_has_entity_name: bool
    entity_description: MetOfficeSensorEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MetOfficeUpdateCoordinator, hass_data: MetOfficeRuntimeData, description: MetOfficeSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def icon(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
