from async_upnp_client.profiles.dlna import PlayMode as _PlayMode
from collections.abc import Mapping
from typing import Any, Final

LOGGER: Any
DOMAIN: Final[str]
CONF_LISTEN_PORT: Final[str]
CONF_CALLBACK_URL_OVERRIDE: Final[str]
CONF_POLL_AVAILABILITY: Final[str]
DEFAULT_NAME: Final[str]
CONNECT_TIMEOUT: Final[int]
PROTOCOL_HTTP: Final[str]
PROTOCOL_RTSP: Final[str]
PROTOCOL_ANY: Final[str]
STREAMABLE_PROTOCOLS: Final[Any]
MEDIA_TYPE_MAP: Mapping[str, str]
MEDIA_UPNP_CLASS_MAP: Mapping[str, str]
MEDIA_METADATA_DIDL: Mapping[str, str]
REPEAT_PLAY_MODES: Mapping[tuple[bool, str], list[_PlayMode]]
SHUFFLE_PLAY_MODES: Mapping[tuple[bool, str], list[_PlayMode]]
