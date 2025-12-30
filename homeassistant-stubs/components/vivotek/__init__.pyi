from .const import CONF_SECURITY_LEVEL as CONF_SECURITY_LEVEL
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_AUTHENTICATION as CONF_AUTHENTICATION, CONF_IP_ADDRESS as CONF_IP_ADDRESS, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, HTTP_DIGEST_AUTHENTICATION as HTTP_DIGEST_AUTHENTICATION, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from libpyvivotek.vivotek import VivotekCamera
from typing import Any

_LOGGER: Incomplete
PLATFORMS: Incomplete
type VivotekConfigEntry = ConfigEntry[VivotekCamera]

def build_cam_client(data: dict[str, Any]) -> VivotekCamera: ...
async def async_build_and_test_cam_client(hass: HomeAssistant, data: dict[str, Any]) -> VivotekCamera: ...
async def async_setup_entry(hass: HomeAssistant, entry: VivotekConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VivotekConfigEntry) -> bool: ...
