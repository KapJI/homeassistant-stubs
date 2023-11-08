from _typeshed import Incomplete
from collections.abc import Callable as Callable
from transmission_rpc import Torrent as Torrent

DOMAIN: str
SWITCH_TYPES: Incomplete
ORDER_NEWEST_FIRST: str
ORDER_OLDEST_FIRST: str
ORDER_BEST_RATIO_FIRST: str
ORDER_WORST_RATIO_FIRST: str
SUPPORTED_ORDER_MODES: dict[str, Callable[[list[Torrent]], list[Torrent]]]
CONF_ENTRY_ID: str
CONF_LIMIT: str
CONF_ORDER: str
DEFAULT_DELETE_DATA: bool
DEFAULT_LIMIT: int
DEFAULT_ORDER = ORDER_OLDEST_FIRST
DEFAULT_NAME: str
DEFAULT_PORT: int
DEFAULT_SCAN_INTERVAL: int
STATE_ATTR_TORRENT_INFO: str
ATTR_DELETE_DATA: str
ATTR_TORRENT: str
SERVICE_ADD_TORRENT: str
SERVICE_REMOVE_TORRENT: str
SERVICE_START_TORRENT: str
SERVICE_STOP_TORRENT: str
EVENT_STARTED_TORRENT: str
EVENT_REMOVED_TORRENT: str
EVENT_DOWNLOADED_TORRENT: str
STATE_UP_DOWN: str
STATE_SEEDING: str
STATE_DOWNLOADING: str