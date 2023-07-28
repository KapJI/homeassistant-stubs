from . import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ToloLampModeSelect(ToloSaunaCoordinatorEntity, SelectEntity):
    _attr_entity_category: Incomplete
    _attr_icon: str
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ConfigEntry) -> None: ...
    @property
    def current_option(self) -> str: ...
    def select_option(self, option: str) -> None: ...
