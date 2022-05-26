from .const import DOMAIN as DOMAIN, STATES_MAP as STATES_MAP, SUPPORTED_FEATURES as SUPPORTED_FEATURES
from .model import DoorDevice as DoorDevice
from _typeshed import Incomplete
from aladdin_connect import AladdinConnectClient as AladdinConnectClient
from homeassistant.components.cover import CoverDeviceClass as CoverDeviceClass, CoverEntity as CoverEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPENING as STATE_OPENING
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import PlatformNotReady as PlatformNotReady
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final

_LOGGER: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AladdinDevice(CoverEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _acc: Incomplete
    _device_id: Incomplete
    _number: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, acc: AladdinConnectClient, device: DoorDevice) -> None: ...
    def close_cover(self, **kwargs: Any) -> None: ...
    def open_cover(self, **kwargs: Any) -> None: ...
    _attr_is_opening: Incomplete
    _attr_is_closing: Incomplete
    _attr_is_closed: Incomplete
    def update(self) -> None: ...
