from _typeshed import Incomplete
from homeassistant.components.tts import CONF_LANG as CONF_LANG, PLATFORM_SCHEMA as PLATFORM_SCHEMA, Provider as Provider, TtsAudioType as TtsAudioType
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

SUPPORT_LANGUAGES: Incomplete
DEFAULT_LANG: str

def get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Provider: ...

class DemoProvider(Provider):
    _lang: Incomplete
    name: str
    def __init__(self, lang: str) -> None: ...
    @property
    def default_language(self) -> str: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def supported_options(self) -> list[str]: ...
    def get_tts_audio(self, message: str, language: str, options: Union[dict[str, Any], None] = ...) -> TtsAudioType: ...
