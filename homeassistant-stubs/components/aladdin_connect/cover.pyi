from .const import NOTIFICATION_ID as NOTIFICATION_ID, NOTIFICATION_TITLE as NOTIFICATION_TITLE, STATES_MAP as STATES_MAP, SUPPORTED_FEATURES as SUPPORTED_FEATURES
from .model import DoorDevice as DoorDevice
from aladdin_connect import AladdinConnectClient
from homeassistant.components.cover import CoverEntity as CoverEntity, DEVICE_CLASS_GARAGE as DEVICE_CLASS_GARAGE
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final

_LOGGER: Final[Any]
PLATFORM_SCHEMA: Final[Any]

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class AladdinDevice(CoverEntity):
    _attr_device_class: Any
    _attr_supported_features: Any
    _acc: Any
    _device_id: Any
    _number: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, acc: AladdinConnectClient, device: DoorDevice) -> None: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    _attr_is_opening: Any
    _attr_is_closing: Any
    _attr_is_closed: Any
    def update(self) -> None: ...
