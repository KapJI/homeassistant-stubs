from .const import DOMAIN as DOMAIN
from .coordinator import SleepIQData as SleepIQData, SleepIQDataUpdateCoordinator as SleepIQDataUpdateCoordinator
from .entity import SleepIQBedEntity as SleepIQBedEntity
from _typeshed import Incomplete
from asyncsleepiq import SleepIQBed as SleepIQBed, SleepIQPreset as SleepIQPreset
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SleepIQSelectEntity(SleepIQBedEntity[SleepIQDataUpdateCoordinator], SelectEntity):
    preset: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, coordinator: SleepIQDataUpdateCoordinator, bed: SleepIQBed, preset: SleepIQPreset) -> None: ...
    _attr_current_option: Incomplete
    def _async_update_attrs(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
