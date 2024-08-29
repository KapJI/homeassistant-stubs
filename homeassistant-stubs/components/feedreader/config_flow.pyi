import feedparser
from .const import CONF_MAX_ENTRIES as CONF_MAX_ENTRIES, DEFAULT_MAX_ENTRIES as DEFAULT_MAX_ENTRIES, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.selector import TextSelector as TextSelector, TextSelectorConfig as TextSelectorConfig, TextSelectorType as TextSelectorType
from homeassistant.util import slugify as slugify
from typing import Any

LOGGER: Incomplete

async def async_fetch_feed(hass: HomeAssistant, url: str) -> feedparser.FeedParserDict: ...

class FeedReaderConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    _config_entry: ConfigEntry
    _max_entries: int | None
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...
    def show_user_form(self, user_input: dict[str, Any] | None = None, errors: dict[str, str] | None = None, description_placeholders: dict[str, str] | None = None, step_id: str = 'user') -> ConfigFlowResult: ...
    def abort_on_import_error(self, url: str, error: str) -> ConfigFlowResult: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_reconfigure(self, _: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_reconfigure_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...

class FeedReaderOptionsFlowHandler(OptionsFlowWithConfigEntry):
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
