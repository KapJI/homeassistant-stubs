import voluptuous as vol
from .const import CONF_MODEL as CONF_MODEL, CONF_VOICE as CONF_VOICE, DEFAULT_MODEL as DEFAULT_MODEL, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult, OptionsFlow as OptionsFlow, OptionsFlowWithConfigEntry as OptionsFlowWithConfigEntry
from homeassistant.const import CONF_API_KEY as CONF_API_KEY
from homeassistant.helpers.selector import SelectOptionDict as SelectOptionDict, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig
from typing import Any

USER_STEP_SCHEMA: Incomplete
_LOGGER: Incomplete

async def get_voices_models(api_key: str) -> tuple[dict[str, str], dict[str, str]]: ...

class ElevenLabsConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    @staticmethod
    def async_get_options_flow(config_entry: ConfigEntry) -> OptionsFlow: ...

class ElevenLabsOptionsFlow(OptionsFlowWithConfigEntry):
    api_key: Incomplete
    voices: Incomplete
    models: Incomplete
    def __init__(self, config_entry: ConfigEntry) -> None: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    def elevenlabs_config_option_schema(self) -> vol.Schema: ...
