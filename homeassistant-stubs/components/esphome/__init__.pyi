from . import dashboard as dashboard, ffmpeg_proxy as ffmpeg_proxy
from .const import CONF_BLUETOOTH_MAC_ADDRESS as CONF_BLUETOOTH_MAC_ADDRESS, CONF_NOISE_PSK as CONF_NOISE_PSK, DOMAIN as DOMAIN
from .domain_data import DomainData as DomainData
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, RuntimeEntryData as RuntimeEntryData
from .manager import DEVICE_CONFLICT_ISSUE_FORMAT as DEVICE_CONFLICT_ISSUE_FORMAT, ESPHomeManager as ESPHomeManager, cleanup_instance as cleanup_instance
from _typeshed import Incomplete
from homeassistant.components import zeroconf as zeroconf
from homeassistant.components.bluetooth import async_remove_scanner as async_remove_scanner
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete
CLIENT_INFO: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> bool: ...
async def async_remove_entry(hass: HomeAssistant, entry: ESPHomeConfigEntry) -> None: ...
