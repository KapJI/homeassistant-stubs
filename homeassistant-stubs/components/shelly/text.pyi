from .coordinator import ShellyConfigEntry as ShellyConfigEntry
from .entity import RpcEntityDescription as RpcEntityDescription, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_orphaned_virtual_entities as async_remove_orphaned_virtual_entities, get_device_entry_gen as get_device_entry_gen, get_virtual_component_ids as get_virtual_component_ids
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.text import TextEntity as TextEntity, TextEntityDescription as TextEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class RpcTextDescription(RpcEntityDescription, TextEntityDescription):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=..., native_min=..., native_max=..., mode=..., pattern=..., sub_key, value=..., available=..., removal_condition=..., extra_state_attributes=..., use_polling_coordinator=..., supported=..., unit=..., options_fn=...) -> None: ...

RPC_TEXT_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RpcText(ShellyRpcAttributeEntity, TextEntity):
    entity_description: RpcTextDescription
    @property
    def native_value(self) -> str | None: ...
    async def async_set_value(self, value: str) -> None: ...
