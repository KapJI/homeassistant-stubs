from .const import DATA_CLIENT as DATA_CLIENT, DOMAIN as DOMAIN
from .helpers import get_home_and_node_id_from_device_entry as get_home_and_node_id_from_device_entry
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from zwave_js_server.client import Client as Client
from zwave_js_server.model.node import NodeDataType as NodeDataType

async def async_get_config_entry_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry) -> list[dict]: ...
async def async_get_device_diagnostics(hass: HomeAssistant, config_entry: ConfigEntry, device: dr.DeviceEntry) -> NodeDataType: ...
