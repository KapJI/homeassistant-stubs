from .const import DOMAIN as DOMAIN
from .entity import VelbusEntity as VelbusEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from velbusaio.channels import SelectedProgram as SelectedProgram

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusSelect(VelbusEntity, SelectEntity):
    _channel: SelectedProgram
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, channel: SelectedProgram) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str: ...
