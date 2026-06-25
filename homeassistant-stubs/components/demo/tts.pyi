from _typeshed import Incomplete
from homeassistant.components.tts import CONF_LANG as CONF_LANG, Provider as Provider, TtsAudioType as TtsAudioType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, override

SUPPORT_LANGUAGES: Incomplete
DEFAULT_LANG: str
PLATFORM_SCHEMA: Incomplete

def get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> Provider: ...

class DemoProvider(Provider):
    _lang: Incomplete
    name: str
    def __init__(self, lang: str) -> None: ...
    @property
    @override
    def default_language(self) -> str: ...
    @property
    @override
    def supported_languages(self) -> list[str]: ...
    @property
    @override
    def supported_options(self) -> list[str]: ...
    @override
    def get_tts_audio(self, message: str, language: str, options: dict[str, Any]) -> TtsAudioType: ...
