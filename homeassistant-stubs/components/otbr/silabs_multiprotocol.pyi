from . import DOMAIN as DOMAIN
from .util import OTBRData as OTBRData
from _typeshed import Incomplete
from homeassistant.components.homeassistant_hardware.silabs_multiprotocol_addon import is_multiprotocol_url as is_multiprotocol_url
from homeassistant.components.thread import async_add_dataset as async_add_dataset
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError

_LOGGER: Incomplete

async def async_change_channel(hass: HomeAssistant, channel: int, delay: float) -> None: ...
async def async_get_channel(hass: HomeAssistant) -> int | None: ...
async def async_using_multipan(hass: HomeAssistant) -> bool: ...
