import asyncio
from .adapter import MatterAdapter as MatterAdapter
from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

class MatterEntryData:
    adapter: MatterAdapter
    listen_task: asyncio.Task
    def __init__(self, adapter, listen_task) -> None: ...

def get_matter(hass: HomeAssistant) -> MatterAdapter: ...
