import asyncio
from .adapter import MatterAdapter as MatterAdapter
from .const import DOMAIN as DOMAIN, ID_TYPE_DEVICE_ID as ID_TYPE_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr
from matter_server.client.models.node import MatterEndpoint as MatterEndpoint, MatterNode as MatterNode
from matter_server.common.models import ServerInfoMessage as ServerInfoMessage

class MatterEntryData:
    adapter: MatterAdapter
    listen_task: asyncio.Task
    def __init__(self, adapter, listen_task) -> None: ...

def get_matter(hass: HomeAssistant) -> MatterAdapter: ...
def get_operational_instance_id(server_info: ServerInfoMessage, node: MatterNode) -> str: ...
def get_device_id(server_info: ServerInfoMessage, endpoint: MatterEndpoint) -> str: ...
async def get_node_from_device_entry(hass: HomeAssistant, device: dr.DeviceEntry) -> MatterNode | None: ...
