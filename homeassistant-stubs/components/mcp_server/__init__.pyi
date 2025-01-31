from .const import DOMAIN as DOMAIN
from .types import MCPServerConfigEntry
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

__all__ = ['CONFIG_SCHEMA', 'DOMAIN', 'async_setup', 'async_setup_entry', 'async_unload_entry']

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: MCPServerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: MCPServerConfigEntry) -> bool: ...
