from .const import DOMAIN as DOMAIN
from bsblan import BSBLAN as BSBLAN
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

async def async_sync_device_time(client: BSBLAN, device_name: str) -> None: ...
