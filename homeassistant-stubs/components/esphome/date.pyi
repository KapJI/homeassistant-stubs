from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from aioesphomeapi import DateInfo, DateState
from datetime import date
from homeassistant.components.date import DateEntity as DateEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeDate(EsphomeEntity[DateInfo, DateState], DateEntity):
    @property
    def native_value(self) -> date | None: ...
    async def async_set_value(self, value: date) -> None: ...