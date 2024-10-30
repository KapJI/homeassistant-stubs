from .entity import CambridgeAudioEntity as CambridgeAudioEntity
from _typeshed import Incomplete
from aiostreammagic import StreamMagicClient as StreamMagicClient
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

@dataclass(frozen=True, kw_only=True)
class CambridgeAudioSwitchEntityDescription(SwitchEntityDescription):
    value_fn: Callable[[StreamMagicClient], bool]
    set_value_fn: Callable[[StreamMagicClient, bool], Awaitable[None]]
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., value_fn, set_value_fn) -> None: ...

CONTROL_ENTITIES: tuple[CambridgeAudioSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CambridgeAudioSwitch(CambridgeAudioEntity, SwitchEntity):
    entity_description: CambridgeAudioSwitchEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, client: StreamMagicClient, description: CambridgeAudioSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
