from .const import DOMAIN as DOMAIN
from .entity import DoorBirdEntity as DoorBirdEntity
from .models import DoorBirdData as DoorBirdData
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from doorbirdpy import DoorBird as DoorBird
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

IR_RELAY: str

@dataclass(frozen=True, kw_only=True)
class DoorbirdButtonEntityDescription(ButtonEntityDescription):
    press_action: Callable[[DoorBird, str], None]
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, press_action) -> None: ...

RELAY_ENTITY_DESCRIPTION: Incomplete
IR_ENTITY_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DoorBirdButton(DoorBirdEntity, ButtonEntity):
    entity_description: DoorbirdButtonEntityDescription
    _relay: Incomplete
    _attr_name: str
    _attr_unique_id: Incomplete
    def __init__(self, door_bird_data: DoorBirdData, relay: str, entity_description: DoorbirdButtonEntityDescription) -> None: ...
    def press(self) -> None: ...
