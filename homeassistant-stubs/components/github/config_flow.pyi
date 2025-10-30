import asyncio
from .const import CLIENT_ID as CLIENT_ID, CONF_REPOSITORIES as CONF_REPOSITORIES, DEFAULT_REPOSITORIES as DEFAULT_REPOSITORIES, DOMAIN as DOMAIN, LOGGER as LOGGER
from aiogithubapi import GitHubDeviceAPI, GitHubLoginDeviceModel as GitHubLoginDeviceModel, GitHubLoginOauthModel as GitHubLoginOauthModel
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlowWithReload as OptionsFlowWithReload
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import SERVER_SOFTWARE as SERVER_SOFTWARE, async_get_clientsession as async_get_clientsession
from typing import Any

async def get_repositories(hass: HomeAssistant, access_token: str) -> list[str]: ...

class GitHubConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    login_task: asyncio.Task | None
    _device: GitHubDeviceAPI | None
    _login: GitHubLoginOauthModel | None
    _login_device: GitHubLoginDeviceModel | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_device(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_repositories(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_could_not_register(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    @callback
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(OptionsFlowWithReload):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
