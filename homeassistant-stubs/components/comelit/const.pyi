from _typeshed import Incomplete
from aiocomelit.api import ComelitSerialBridgeObject, ComelitVedoAreaObject, ComelitVedoZoneObject

_LOGGER: Incomplete
ObjectClassType = ComelitSerialBridgeObject | ComelitVedoAreaObject | ComelitVedoZoneObject
DOMAIN: str
DEFAULT_PORT: int
DEVICE_TYPE_LIST: Incomplete
SCAN_INTERVAL: int
PRESET_MODE_AUTO: str
PRESET_MODE_MANUAL: str
PRESET_MODE_AUTO_TARGET_TEMP: int
