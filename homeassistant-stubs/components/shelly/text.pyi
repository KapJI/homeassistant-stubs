from .coordinator import ShellyConfigEntry as ShellyConfigEntry
from .entity import RpcEntityDescription as RpcEntityDescription, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, async_setup_entry_rpc as async_setup_entry_rpc, rpc_call as rpc_call
from .utils import async_remove_orphaned_entities as async_remove_orphaned_entities, get_device_entry_gen as get_device_entry_gen, get_virtual_component_ids as get_virtual_component_ids
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.text import TextEntity as TextEntity, TextEntityDescription as TextEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

@dataclass(frozen=True, kw_only=True)
class RpcTextDescription(RpcEntityDescription, TextEntityDescription): ...

RPC_TEXT_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RpcText(ShellyRpcAttributeEntity, TextEntity):
    entity_description: RpcTextDescription
    attribute_value: str | None
    _id: int
    @property
    def native_value(self) -> str | None: ...
    @rpc_call
    async def async_set_value(self, value: str) -> None: ...
