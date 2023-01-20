from .const import DOMAIN as DOMAIN, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID, ID_TYPE_SERIAL as ID_TYPE_SERIAL, LOGGER as LOGGER
from .device_platform import DEVICE_PLATFORM as DEVICE_PLATFORM
from .helpers import get_device_id as get_device_id
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from matter_server.client import MatterClient as MatterClient
from matter_server.common.models.node import MatterNode as MatterNode
from matter_server.common.models.node_device import AbstractMatterNodeDevice as AbstractMatterNodeDevice

class MatterAdapter:
    matter_client: Incomplete
    hass: Incomplete
    config_entry: Incomplete
    platform_handlers: Incomplete
    def __init__(self, hass: HomeAssistant, matter_client: MatterClient, config_entry: ConfigEntry) -> None: ...
    def register_platform_handler(self, platform: Platform, add_entities: AddEntitiesCallback) -> None: ...
    async def setup_nodes(self) -> None: ...
    def _setup_node(self, node: MatterNode) -> None: ...
    def _create_device_registry(self, node_device: AbstractMatterNodeDevice, bridge_unique_id: Union[str, None] = ...) -> None: ...
    def _setup_node_device(self, node_device: AbstractMatterNodeDevice, bridge_unique_id: Union[str, None]) -> None: ...
