from . import GuardianData as GuardianData, PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .const import API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, CONF_UID as CONF_UID, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from .coordinator import GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator
from .util import EntityDomainReplacementStrategy as EntityDomainReplacementStrategy, async_finish_entity_domain_replacements as async_finish_entity_domain_replacements
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ATTR_CONNECTED_CLIENTS: str
SENSOR_KIND_LEAK_DETECTED: str
SENSOR_KIND_MOVED: str

@dataclass(frozen=True, kw_only=True)
class PairedSensorBinarySensorDescription(BinarySensorEntityDescription):
    is_on_fn: Callable[[dict[str, Any]], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, is_on_fn) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValveControllerBinarySensorDescription(BinarySensorEntityDescription, ValveControllerEntityDescription):
    is_on_fn: Callable[[dict[str, Any]], bool]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, api_category, is_on_fn) -> None: ...

PAIRED_SENSOR_DESCRIPTIONS: Incomplete
VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorBinarySensor(PairedSensorEntity, BinarySensorEntity):
    entity_description: PairedSensorBinarySensorDescription
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinator: GuardianDataUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...

class ValveControllerBinarySensor(ValveControllerEntity, BinarySensorEntity):
    entity_description: ValveControllerBinarySensorDescription
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, GuardianDataUpdateCoordinator], description: ValveControllerBinarySensorDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
