from .entity import CambridgeAudioEntity as CambridgeAudioEntity
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

@dataclass(frozen=True, kw_only=True)
class CambridgeAudioSelectEntityDescription(SelectEntityDescription):
    options_fn: Callable[[StreamMagicClient], list[str]] = ...
    load_fn: Callable[[StreamMagicClient], bool] = ...
    value_fn: Callable[[StreamMagicClient], str | None]
    set_value_fn: Callable[[StreamMagicClient, str], Awaitable[None]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., options=..., options_fn=..., load_fn=..., value_fn, set_value_fn) -> None: ...

async def _audio_output_set_value_fn(client: StreamMagicClient, value: str) -> None: ...
def _audio_output_value_fn(client: StreamMagicClient) -> str | None: ...

CONTROL_ENTITIES: tuple[CambridgeAudioSelectEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CambridgeAudioSelect(CambridgeAudioEntity, SelectEntity):
    entity_description: CambridgeAudioSelectEntityDescription
    _attr_unique_id: Incomplete
    _attr_options: Incomplete
    def __init__(self, client: StreamMagicClient, description: CambridgeAudioSelectEntityDescription) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
