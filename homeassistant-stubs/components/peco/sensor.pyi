from .const import ATTR_CONTENT as ATTR_CONTENT, CONF_COUNTY as CONF_COUNTY, DOMAIN as DOMAIN
from .coordinator import PECOCoordinatorData as PECOCoordinatorData, PecoConfigEntry as PecoConfigEntry, PecoOutageCoordinator as PecoOutageCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Final

@dataclass(frozen=True, kw_only=True)
class PECOSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[PECOCoordinatorData], int | str]
    attribute_fn: Callable[[PECOCoordinatorData], dict[str, str]]

PARALLEL_UPDATES: Final[int]
SENSOR_LIST: tuple[PECOSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: PecoConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PecoSensor(CoordinatorEntity[PecoOutageCoordinator], SensorEntity):
    entity_description: PECOSensorEntityDescription
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, description: PECOSensorEntityDescription, county: str, coordinator: PecoOutageCoordinator) -> None: ...
    @property
    def native_value(self) -> int | str: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
