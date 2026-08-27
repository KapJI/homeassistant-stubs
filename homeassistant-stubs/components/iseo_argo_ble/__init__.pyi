from .const import CONF_PRIV_SCALAR as CONF_PRIV_SCALAR, DEFAULT_USER_SUBTYPE as DEFAULT_USER_SUBTYPE, DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from _typeshed import Incomplete
from homeassistant.components.bluetooth import async_ble_device_from_address as async_ble_device_from_address
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_UUID as CONF_UUID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from iseo_argo_ble import IseoClient

CONFIG_SCHEMA: Incomplete
type IseoConfigEntry = ConfigEntry[IseoClient]

async def async_setup_entry(hass: HomeAssistant, entry: IseoConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: IseoConfigEntry) -> bool: ...
