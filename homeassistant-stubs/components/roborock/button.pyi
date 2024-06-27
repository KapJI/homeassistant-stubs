from . import RoborockCoordinators as RoborockCoordinators
from .const import DOMAIN as DOMAIN
from .coordinator import RoborockDataUpdateCoordinator as RoborockDataUpdateCoordinator
from .device import RoborockEntityV1 as RoborockEntityV1
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from roborock.roborock_typing import RoborockCommand

@dataclass(frozen=True, kw_only=True)
class RoborockButtonDescription(ButtonEntityDescription):
    command: RoborockCommand
    param: list | dict | None
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, command, param) -> None: ...

CONSUMABLE_BUTTON_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RoborockButtonEntity(RoborockEntityV1, ButtonEntity):
    entity_description: RoborockButtonDescription
    def __init__(self, coordinator: RoborockDataUpdateCoordinator, entity_description: RoborockButtonDescription) -> None: ...
    async def async_press(self) -> None: ...
