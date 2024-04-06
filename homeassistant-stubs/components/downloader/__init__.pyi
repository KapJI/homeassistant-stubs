from .const import ATTR_FILENAME as ATTR_FILENAME, ATTR_OVERWRITE as ATTR_OVERWRITE, ATTR_SUBDIR as ATTR_SUBDIR, ATTR_URL as ATTR_URL, CONF_DOWNLOAD_DIR as CONF_DOWNLOAD_DIR, DOMAIN as DOMAIN, DOWNLOAD_COMPLETED_EVENT as DOWNLOAD_COMPLETED_EVENT, DOWNLOAD_FAILED_EVENT as DOWNLOAD_FAILED_EVENT, SERVICE_DOWNLOAD_FILE as SERVICE_DOWNLOAD_FILE, _LOGGER as _LOGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.service import async_register_admin_service as async_register_admin_service
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename, raise_if_invalid_path as raise_if_invalid_path

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_import_config(hass: HomeAssistant, config: ConfigType) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
