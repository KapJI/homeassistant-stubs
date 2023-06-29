import abc
from .const import DOMAIN as DOMAIN
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneAidooEntity as AirzoneAidooEntity, AirzoneEntity as AirzoneEntity, AirzoneWebServerEntity as AirzoneWebServerEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT, UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

AIDOO_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]
WEBSERVER_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]
ZONE_SENSOR_TYPES: Final[tuple[SensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneSensor(AirzoneEntity, SensorEntity, metaclass=abc.ABCMeta):
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    def _async_update_attrs(self) -> None: ...

class AirzoneAidooSensor(AirzoneAidooEntity, AirzoneSensor):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, aidoo_id: str, aidoo_data: dict[str, Any]) -> None: ...

class AirzoneWebServerSensor(AirzoneWebServerEntity, AirzoneSensor):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, ws_id: str, ws_data: dict[str, Any]) -> None: ...

class AirzoneZoneSensor(AirzoneZoneEntity, AirzoneSensor):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: SensorEntityDescription, zone_id: str, zone_data: dict[str, Any]) -> None: ...
