from . import SFTPConfigEntryData as SFTPConfigEntryData
from .client import get_client_options as get_client_options
from .const import CONF_BACKUP_LOCATION as CONF_BACKUP_LOCATION, CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PRIVATE_KEY_FILE as CONF_PRIVATE_KEY_FILE, CONF_USERNAME as CONF_USERNAME, DEFAULT_PKEY_NAME as DEFAULT_PKEY_NAME, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from homeassistant.components.file_upload import process_uploaded_file as process_uploaded_file
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.selector import FileSelector as FileSelector, FileSelectorConfig as FileSelectorConfig, TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.util.ulid import ulid as ulid
from typing import Any

DATA_SCHEMA: Incomplete

class SFTPStorageException(Exception): ...
class SFTPStorageInvalidPrivateKey(SFTPStorageException): ...
class SFTPStorageMissingPasswordOrPkey(SFTPStorageException): ...

class SFTPFlowHandler(ConfigFlow, domain=DOMAIN):
    _client_keys: list
    def __init__(self) -> None: ...
    async def _validate_auth_and_save_keyfile(self, user_input: dict[str, Any]) -> dict[str, Any]: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None, step_id: str = 'user') -> ConfigFlowResult: ...

async def save_uploaded_pkey_file(hass: HomeAssistant, uploaded_file_id: str) -> str: ...
