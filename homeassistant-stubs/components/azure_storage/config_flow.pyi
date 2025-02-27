from .const import CONF_ACCOUNT_NAME as CONF_ACCOUNT_NAME, CONF_CONTAINER_NAME as CONF_CONTAINER_NAME, CONF_STORAGE_ACCOUNT_KEY as CONF_STORAGE_ACCOUNT_KEY, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from typing import Any

_LOGGER: Incomplete

class AzureStorageConfigFlow(ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
