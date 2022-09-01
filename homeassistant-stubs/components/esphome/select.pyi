from . import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import SelectInfo, SelectState
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeSelect(EsphomeEntity[SelectInfo, SelectState], SelectEntity):
    @property
    def options(self) -> list[str]: ...
    @property
    def current_option(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...
