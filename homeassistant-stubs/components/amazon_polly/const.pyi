from typing import Final

CONF_REGION: Final[str]
CONF_ACCESS_KEY_ID: Final[str]
CONF_SECRET_ACCESS_KEY: Final[str]
CONF_ENGINE: Final[str]
CONF_VOICE: Final[str]
CONF_OUTPUT_FORMAT: Final[str]
CONF_SAMPLE_RATE: Final[str]
CONF_TEXT_TYPE: Final[str]
SUPPORTED_OUTPUT_FORMATS: Final[set[str]]
SUPPORTED_SAMPLE_RATES: Final[set[str]]
SUPPORTED_SAMPLE_RATES_MAP: Final[dict[str, set[str]]]
SUPPORTED_TEXT_TYPES: Final[set[str]]
CONTENT_TYPE_EXTENSIONS: Final[dict[str, str]]
DEFAULT_REGION: Final[str]
DEFAULT_ENGINE: Final[str]
DEFAULT_VOICE: Final[str]
DEFAULT_OUTPUT_FORMAT: Final[str]
DEFAULT_TEXT_TYPE: Final[str]
DEFAULT_SAMPLE_RATES: Final[dict[str, str]]
AWS_CONF_CONNECT_TIMEOUT: Final[int]
AWS_CONF_READ_TIMEOUT: Final[int]
AWS_CONF_MAX_POOL_CONNECTIONS: Final[int]
