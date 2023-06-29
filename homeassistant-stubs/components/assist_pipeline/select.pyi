from .const import DOMAIN as DOMAIN
from .pipeline import PipelineData as PipelineData, PipelineStorageCollection as PipelineStorageCollection
from .vad import VadSensitivity as VadSensitivity
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import collection as collection, restore_state as restore_state

OPTION_PREFERRED: str

def get_chosen_pipeline(hass: HomeAssistant, domain: str, unique_id_prefix: str) -> str | None: ...
def get_vad_sensitivity(hass: HomeAssistant, domain: str, unique_id_prefix: str) -> VadSensitivity: ...

class AssistPipelineSelect(SelectEntity, restore_state.RestoreEntity):
    entity_description: Incomplete
    _attr_should_poll: bool
    _attr_current_option = OPTION_PREFERRED
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, unique_id_prefix: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
    async def _pipelines_updated(self, change_sets: Iterable[collection.CollectionChangeSet]) -> None: ...
    def _update_options(self) -> None: ...

class VadSensitivitySelect(SelectEntity, restore_state.RestoreEntity):
    entity_description: Incomplete
    _attr_should_poll: bool
    _attr_current_option: Incomplete
    _attr_options: Incomplete
    _attr_unique_id: Incomplete
    hass: Incomplete
    def __init__(self, hass: HomeAssistant, unique_id_prefix: str) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_select_option(self, option: str) -> None: ...
