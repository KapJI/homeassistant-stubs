from .api import AsyncConfigEntryAuth as AsyncConfigEntryAuth
from .const import AFFECTS_TO_ACTIVE_PROGRAM as AFFECTS_TO_ACTIVE_PROGRAM, AFFECTS_TO_SELECTED_PROGRAM as AFFECTS_TO_SELECTED_PROGRAM, ATTR_AFFECTS_TO as ATTR_AFFECTS_TO, ATTR_KEY as ATTR_KEY, ATTR_PROGRAM as ATTR_PROGRAM, ATTR_UNIT as ATTR_UNIT, ATTR_VALUE as ATTR_VALUE, DOMAIN as DOMAIN, OLD_NEW_UNIQUE_ID_SUFFIX_MAP as OLD_NEW_UNIQUE_ID_SUFFIX_MAP, PROGRAM_ENUM_OPTIONS as PROGRAM_ENUM_OPTIONS, SERVICE_OPTION_ACTIVE as SERVICE_OPTION_ACTIVE, SERVICE_OPTION_SELECTED as SERVICE_OPTION_SELECTED, SERVICE_PAUSE_PROGRAM as SERVICE_PAUSE_PROGRAM, SERVICE_RESUME_PROGRAM as SERVICE_RESUME_PROGRAM, SERVICE_SELECT_PROGRAM as SERVICE_SELECT_PROGRAM, SERVICE_SETTING as SERVICE_SETTING, SERVICE_SET_PROGRAM_AND_OPTIONS as SERVICE_SET_PROGRAM_AND_OPTIONS, SERVICE_START_PROGRAM as SERVICE_START_PROGRAM, SVE_TRANSLATION_PLACEHOLDER_KEY as SVE_TRANSLATION_PLACEHOLDER_KEY, SVE_TRANSLATION_PLACEHOLDER_PROGRAM as SVE_TRANSLATION_PLACEHOLDER_PROGRAM, SVE_TRANSLATION_PLACEHOLDER_VALUE as SVE_TRANSLATION_PLACEHOLDER_VALUE, TRANSLATION_KEYS_PROGRAMS_MAP as TRANSLATION_KEYS_PROGRAMS_MAP
from .coordinator import HomeConnectConfigEntry as HomeConnectConfigEntry, HomeConnectCoordinator as HomeConnectCoordinator
from .utils import bsh_key_to_translation_key as bsh_key_to_translation_key, get_dict_from_home_connect_error as get_dict_from_home_connect_error
from _typeshed import Incomplete
from aiohomeconnect.client import Client as HomeConnectClient
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers import config_entry_oauth2_flow as config_entry_oauth2_flow
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry, async_migrate_entries as async_migrate_entries
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, async_delete_issue as async_delete_issue
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete
PROGRAM_OPTIONS: Incomplete
SERVICE_SETTING_SCHEMA: Incomplete
SERVICE_OPTION_SCHEMA: Incomplete
SERVICE_PROGRAM_SCHEMA: Incomplete

def _require_program_or_at_least_one_option(data: dict) -> dict: ...

SERVICE_PROGRAM_AND_OPTIONS_SCHEMA: Incomplete
SERVICE_COMMAND_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def _get_client_and_ha_id(hass: HomeAssistant, device_id: str) -> tuple[HomeConnectClient, str]: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry) -> bool: ...
