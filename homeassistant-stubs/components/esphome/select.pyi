from .const import DOMAIN as DOMAIN
from .entity import EsphomeAssistEntity as EsphomeAssistEntity, EsphomeEntity as EsphomeEntity, convert_api_error_ha_error as convert_api_error_ha_error, esphome_state_property as esphome_state_property, platform_async_setup_entry as platform_async_setup_entry
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import EntityInfo as EntityInfo, SelectInfo, SelectState
from homeassistant.components.assist_pipeline.select import AssistPipelineSelect as AssistPipelineSelect, VadSensitivitySelect as VadSensitivitySelect
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EsphomeSelect(EsphomeEntity[SelectInfo, SelectState], SelectEntity):
    _attr_options: Incomplete
    def _on_static_info_update(self, static_info: EntityInfo) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...

class EsphomeAssistPipelineSelect(EsphomeAssistEntity, AssistPipelineSelect):
    def __init__(self, hass: HomeAssistant, entry_data: RuntimeEntryData) -> None: ...

class EsphomeVadSensitivitySelect(EsphomeAssistEntity, VadSensitivitySelect):
    def __init__(self, hass: HomeAssistant, entry_data: RuntimeEntryData) -> None: ...
