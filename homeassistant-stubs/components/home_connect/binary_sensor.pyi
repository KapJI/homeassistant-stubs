from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import BSH_DOOR_STATE_CLOSED as BSH_DOOR_STATE_CLOSED, BSH_DOOR_STATE_LOCKED as BSH_DOOR_STATE_LOCKED, BSH_DOOR_STATE_OPEN as BSH_DOOR_STATE_OPEN, DOMAIN as DOMAIN, REFRIGERATION_STATUS_DOOR_CLOSED as REFRIGERATION_STATUS_DOOR_CLOSED, REFRIGERATION_STATUS_DOOR_OPEN as REFRIGERATION_STATUS_DOOR_OPEN
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry, HomeConnectCoordinator as HomeConnectCoordinator
from .entity import HomeConnectEntity as HomeConnectEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue

PARALLEL_UPDATES: int
REFRIGERATION_DOOR_BOOLEAN_MAP: Incomplete

@dataclass(frozen=True, kw_only=True)
class HomeConnectBinarySensorEntityDescription(BinarySensorEntityDescription):
    boolean_map: dict[str, bool] | None = ...

BINARY_SENSORS: Incomplete
CONNECTED_BINARY_ENTITY_DESCRIPTION: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectBinarySensor(HomeConnectEntity, BinarySensorEntity):
    entity_description: HomeConnectBinarySensorEntityDescription
    _attr_is_on: Incomplete
    def update_native_value(self) -> None: ...

class HomeConnectConnectivityBinarySensor(HomeConnectEntity, BinarySensorEntity):
    _attr_entity_category: Incomplete
    _attr_is_on: Incomplete
    def update_native_value(self) -> None: ...
    @property
    def available(self) -> bool: ...

class HomeConnectDoorBinarySensor(HomeConnectBinarySensor):
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: HomeConnectCoordinator, appliance: HomeConnectApplianceData) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
