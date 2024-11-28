from . import AutomowerConfigEntry as AutomowerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import AutomowerDataUpdateCoordinator as AutomowerDataUpdateCoordinator
from .entity import AutomowerBaseEntity as AutomowerBaseEntity
from _typeshed import Incomplete
from aioautomower.model import MowerAttributes as MowerAttributes
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue

_LOGGER: Incomplete

def entity_used_in(hass: HomeAssistant, entity_id: str) -> list[str]: ...

@dataclass(frozen=True, kw_only=True)
class AutomowerBinarySensorEntityDescription(BinarySensorEntityDescription):
    value_fn: Callable[[MowerAttributes], bool]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., value_fn) -> None: ...

MOWER_BINARY_SENSOR_TYPES: tuple[AutomowerBinarySensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: AutomowerConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AutomowerBinarySensorEntity(AutomowerBaseEntity, BinarySensorEntity):
    entity_description: AutomowerBinarySensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, mower_id: str, coordinator: AutomowerDataUpdateCoordinator, description: AutomowerBinarySensorEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
