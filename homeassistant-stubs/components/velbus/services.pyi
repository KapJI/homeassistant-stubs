from . import VelbusConfigEntry as VelbusConfigEntry
from .const import CONF_CONFIG_ENTRY as CONF_CONFIG_ENTRY, CONF_INTERFACE as CONF_INTERFACE, CONF_MEMO_TEXT as CONF_MEMO_TEXT, DOMAIN as DOMAIN, SERVICE_CLEAR_CACHE as SERVICE_CLEAR_CACHE, SERVICE_SCAN as SERVICE_SCAN, SERVICE_SET_MEMO_TEXT as SERVICE_SET_MEMO_TEXT, SERVICE_SYNC as SERVICE_SYNC
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import selector as selector
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR

def setup_services(hass: HomeAssistant) -> None: ...
