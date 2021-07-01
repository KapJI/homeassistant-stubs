import boto3
from .const import AWS_CONF_CONNECT_TIMEOUT as AWS_CONF_CONNECT_TIMEOUT, AWS_CONF_MAX_POOL_CONNECTIONS as AWS_CONF_MAX_POOL_CONNECTIONS, AWS_CONF_READ_TIMEOUT as AWS_CONF_READ_TIMEOUT, CONF_ACCESS_KEY_ID as CONF_ACCESS_KEY_ID, CONF_ENGINE as CONF_ENGINE, CONF_OUTPUT_FORMAT as CONF_OUTPUT_FORMAT, CONF_REGION as CONF_REGION, CONF_SAMPLE_RATE as CONF_SAMPLE_RATE, CONF_SECRET_ACCESS_KEY as CONF_SECRET_ACCESS_KEY, CONF_TEXT_TYPE as CONF_TEXT_TYPE, CONF_VOICE as CONF_VOICE, CONTENT_TYPE_EXTENSIONS as CONTENT_TYPE_EXTENSIONS, DEFAULT_ENGINE as DEFAULT_ENGINE, DEFAULT_OUTPUT_FORMAT as DEFAULT_OUTPUT_FORMAT, DEFAULT_REGION as DEFAULT_REGION, DEFAULT_SAMPLE_RATES as DEFAULT_SAMPLE_RATES, DEFAULT_TEXT_TYPE as DEFAULT_TEXT_TYPE, DEFAULT_VOICE as DEFAULT_VOICE, SUPPORTED_ENGINES as SUPPORTED_ENGINES, SUPPORTED_OUTPUT_FORMATS as SUPPORTED_OUTPUT_FORMATS, SUPPORTED_REGIONS as SUPPORTED_REGIONS, SUPPORTED_SAMPLE_RATES as SUPPORTED_SAMPLE_RATES, SUPPORTED_SAMPLE_RATES_MAP as SUPPORTED_SAMPLE_RATES_MAP, SUPPORTED_TEXT_TYPES as SUPPORTED_TEXT_TYPES, SUPPORTED_VOICES as SUPPORTED_VOICES
from homeassistant.components.tts import Provider as Provider, TtsAudioType as TtsAudioType
from homeassistant.const import ATTR_CREDENTIALS as ATTR_CREDENTIALS, CONF_PROFILE_NAME as CONF_PROFILE_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final

_LOGGER: Final[Any]
PLATFORM_SCHEMA: Final[Any]

def get_engine(hass: HomeAssistant, config: ConfigType, discovery_info: Union[DiscoveryInfoType, None] = ...) -> Union[Provider, None]: ...

class AmazonPollyProvider(Provider):
    client: Any
    config: Any
    supported_langs: Any
    all_voices: Any
    default_voice: Any
    name: str
    def __init__(self, polly_client: boto3.client, config: ConfigType, supported_languages: list[str], all_voices: dict[str, dict[str, str]]) -> None: ...
    @property
    def supported_languages(self) -> list[str]: ...
    @property
    def default_language(self) -> Union[str, None]: ...
    @property
    def default_options(self) -> dict[str, str]: ...
    @property
    def supported_options(self) -> list[str]: ...
    def get_tts_audio(self, message: str, language: Union[str, None] = ..., options: Union[dict[str, str], None] = ...) -> TtsAudioType: ...
