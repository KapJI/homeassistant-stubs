from .client import CloudClient as CloudClient
from .const import DOMAIN as DOMAIN
from .prefs import CloudPreferences as CloudPreferences
from _typeshed import Incomplete
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.tts import ATTR_AUDIO_OUTPUT as ATTR_AUDIO_OUTPUT, ATTR_VOICE as ATTR_VOICE, CONF_LANG as CONF_LANG, PLATFORM_SCHEMA as PLATFORM_SCHEMA, Provider as Provider, TtsAudioType as TtsAudioType, Voice as Voice
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

ATTR_GENDER: str
SUPPORT_LANGUAGES: Incomplete
_LOGGER: Incomplete

def validate_lang(value: dict[str, Any]) -> dict[str, Any]: ...
async def async_get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = ...) -> CloudProvider: ...

class CloudProvider(Provider):
    cloud: Incomplete
    name: str
    _language: Incomplete
    _gender: Incomplete
    def __init__(self, cloud: Cloud[CloudClient], language: str | None, gender: str | None) -> None: ...
    async def _sync_prefs(self, prefs: CloudPreferences) -> None: ...
    @property
    def default_language(self) -> str | None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_options(self) -> list[str]: ...
    def async_get_supported_voices(self, language: str) -> list[Voice] | None: ...
    @property
    def default_options(self) -> dict[str, Any]: ...
    async def async_get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
