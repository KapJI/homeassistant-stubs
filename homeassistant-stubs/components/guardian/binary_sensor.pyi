from . import GuardianData as GuardianData, PairedSensorEntity as PairedSensorEntity, ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .const import API_SYSTEM_ONBOARD_SENSOR_STATUS as API_SYSTEM_ONBOARD_SENSOR_STATUS, CONF_UID as CONF_UID, DOMAIN as DOMAIN, SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED as SIGNAL_PAIRED_SENSOR_COORDINATOR_ADDED
from .util import EntityDomainReplacementStrategy as EntityDomainReplacementStrategy, GuardianDataUpdateCoordinator as GuardianDataUpdateCoordinator, async_finish_entity_domain_replacements as async_finish_entity_domain_replacements
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

ATTR_CONNECTED_CLIENTS: str
SENSOR_KIND_LEAK_DETECTED: str
SENSOR_KIND_MOVED: str

class ValveControllerBinarySensorDescription(BinarySensorEntityDescription, ValveControllerEntityDescription):
    def __init__(self, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

PAIRED_SENSOR_DESCRIPTIONS: Incomplete
VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PairedSensorBinarySensor(PairedSensorEntity, BinarySensorEntity):
    entity_description: BinarySensorEntityDescription
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinator: GuardianDataUpdateCoordinator, description: BinarySensorEntityDescription) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...

class ValveControllerBinarySensor(ValveControllerEntity, BinarySensorEntity):
    entity_description: ValveControllerBinarySensorDescription
    _attr_is_on: bool
    def __init__(self, entry: ConfigEntry, coordinators: dict[str, GuardianDataUpdateCoordinator], description: ValveControllerBinarySensorDescription) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...
