import asyncio
from .adapter import MatterAdapter as MatterAdapter
from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from matter_server.common.models.node import MatterNode as MatterNode
from matter_server.common.models.node_device import AbstractMatterNodeDevice as AbstractMatterNodeDevice
from matter_server.common.models.server_information import ServerInfo as ServerInfo

class MatterEntryData:
    adapter: MatterAdapter
    listen_task: asyncio.Task
    def __init__(self, adapter, listen_task) -> None: ...

def get_matter(hass: HomeAssistant) -> MatterAdapter: ...
def get_operational_instance_id(server_info: ServerInfo, node: MatterNode) -> str: ...
def get_device_id(server_info: ServerInfo, node_device: AbstractMatterNodeDevice) -> str: ...
