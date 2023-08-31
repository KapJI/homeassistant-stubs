from .const import CONF_COAP_PORT as CONF_COAP_PORT, CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DEFAULT_COAP_PORT as DEFAULT_COAP_PORT, DOMAIN as DOMAIN, LOGGER as LOGGER, PUSH_UPDATE_ISSUE_ID as PUSH_UPDATE_ISSUE_ID
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyEntryData as ShellyEntryData, ShellyRestCoordinator as ShellyRestCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, ShellyRpcPollingCoordinator as ShellyRpcPollingCoordinator, get_entry_data as get_entry_data
from .utils import get_block_device_sleep_period as get_block_device_sleep_period, get_coap_context as get_coap_context, get_device_entry_gen as get_device_entry_gen, get_rpc_device_sleep_period as get_rpc_device_sleep_period, get_rpc_device_wakeup_period as get_rpc_device_wakeup_period, get_ws_context as get_ws_context
from _typeshed import Incomplete
from aioshelly.block_device import BlockUpdateType as BlockUpdateType
from aioshelly.rpc_device import RpcUpdateType as RpcUpdateType
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import CONNECTION_NETWORK_MAC as CONNECTION_NETWORK_MAC, format_mac as format_mac
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Final

BLOCK_PLATFORMS: Final[Incomplete]
BLOCK_SLEEPING_PLATFORMS: Final[Incomplete]
RPC_PLATFORMS: Final[Incomplete]
RPC_SLEEPING_PLATFORMS: Final[Incomplete]
COAP_SCHEMA: Final[Incomplete]
CONFIG_SCHEMA: Final[Incomplete]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_setup_block_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def _async_setup_rpc_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
