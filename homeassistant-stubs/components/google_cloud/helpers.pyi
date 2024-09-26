import voluptuous as vol
from .const import CONF_ENCODING as CONF_ENCODING, CONF_GAIN as CONF_GAIN, CONF_GENDER as CONF_GENDER, CONF_KEY_FILE as CONF_KEY_FILE, CONF_PITCH as CONF_PITCH, CONF_PROFILES as CONF_PROFILES, CONF_SPEED as CONF_SPEED, CONF_TEXT_TYPE as CONF_TEXT_TYPE, CONF_VOICE as CONF_VOICE, DEFAULT_LANG as DEFAULT_LANG
from collections.abc import Mapping
from google.cloud import texttospeech
from homeassistant.components.tts import CONF_LANG as CONF_LANG
from homeassistant.helpers.selector import NumberSelector as NumberSelector, NumberSelectorConfig as NumberSelectorConfig, SelectSelector as SelectSelector, SelectSelectorConfig as SelectSelectorConfig, SelectSelectorMode as SelectSelectorMode
from typing import Any

DEFAULT_VOICE: str

async def async_tts_voices(client: texttospeech.TextToSpeechAsyncClient) -> dict[str, list[str]]: ...
def tts_options_schema(config_options: dict[str, Any], voices: dict[str, list[str]], from_config_flow: bool = False) -> vol.Schema: ...
def tts_platform_schema() -> vol.Schema: ...
def validate_service_account_info(info: Mapping[str, str]) -> None: ...
