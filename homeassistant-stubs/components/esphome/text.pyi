from .entity import EsphomeEntity as EsphomeEntity, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .enum_mapper import EsphomeEnumMapper as EsphomeEnumMapper
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, TextInfo, TextMode as EsphomeTextMode, TextState
from homeassistant.components.text import TextEntity as TextEntity, TextMode as TextMode
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

TEXT_MODES: EsphomeEnumMapper[EsphomeTextMode, TextMode]

class EsphomeText(EsphomeEntity[TextInfo, TextState], TextEntity):
    _attr_native_min: Incomplete
    _attr_native_max: Incomplete
    _attr_pattern: Incomplete
    _attr_mode: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    async def async_set_value(self, value: str) -> None: ...
