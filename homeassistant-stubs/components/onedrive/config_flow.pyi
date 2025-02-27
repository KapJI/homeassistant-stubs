import logging
from .const import CONF_DELETE_PERMANENTLY as CONF_DELETE_PERMANENTLY, CONF_FOLDER_ID as CONF_FOLDER_ID, CONF_FOLDER_NAME as CONF_FOLDER_NAME, DOMAIN as DOMAIN, OAUTH_SCOPES as OAUTH_SCOPES
from .coordinator import OneDriveConfigEntry as OneDriveConfigEntry
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.config_entries import ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, SOURCE_REAUTH as SOURCE_REAUTH, SOURCE_RECONFIGURE as SOURCE_RECONFIGURE, SOURCE_USER as SOURCE_USER
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_TOKEN as CONF_TOKEN
from homeassistant.core import callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.config_entry_oauth2_flow import AbstractOAuth2FlowHandler as AbstractOAuth2FlowHandler
from onedrive_personal_sdk.clients.client import OneDriveClient
from onedrive_personal_sdk.models.items import AppRoot as AppRoot
from typing import Any

FOLDER_NAME_SCHEMA: Incomplete

class OneDriveConfigFlow(AbstractOAuth2FlowHandler, domain=DOMAIN):
    DOMAIN = DOMAIN
    MINOR_VERSION: int
    client: OneDriveClient
    approot: AppRoot
    step_data: dict[str, Any]
    def __init__(self) -> None: ...
    @property
    def logger(self) -> logging.Logger: ...
    @property
    def extra_authorize_data(self) -> dict[str, Any]: ...
    @property
    def apps_folder(self) -> str: ...
    async def async_oauth_create_entry(self, data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_folder_name(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure_folder(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reauth(self, entry_data: Mapping[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reauth_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: OneDriveConfigEntry) -> OneDriveOptionsFlowHandler: ...

class OneDriveOptionsFlowHandler(OptionsFlow):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
