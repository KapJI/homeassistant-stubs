from _typeshed import Incomplete
from aiocomelit.api import ComelitDeviceObject, ComelitVedoAreaObject, ComelitVedoZoneObject

LOGGER: Incomplete
type ObjectClassType = ComelitDeviceObject | ComelitVedoAreaObject | ComelitVedoZoneObject
DOMAIN: str
DEFAULT_PORT: int
DEVICE_TYPE_LIST: Incomplete
CONF_VEDO_PIN: str
SCAN_INTERVAL: int
PRESET_MODE_AUTO: str
PRESET_MODE_MANUAL: str
PRESET_MODE_AUTO_TARGET_TEMP: int
