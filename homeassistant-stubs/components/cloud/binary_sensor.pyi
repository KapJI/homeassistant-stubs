from .client import CloudClient as CloudClient
from .const import DISPATCHER_REMOTE_UPDATE as DISPATCHER_REMOTE_UPDATE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from hass_nabucasa import Cloud as Cloud
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

WAIT_UNTIL_CHANGE: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = ...) -> None: ...

class CloudRemoteBinary(BinarySensorEntity):
    _attr_name: str
    _attr_device_class: Incomplete
    _attr_should_poll: bool
    _attr_unique_id: str
    _attr_entity_category: Incomplete
    cloud: Incomplete
    _unsub_dispatcher: Incomplete
    def __init__(self, cloud: Cloud[CloudClient]) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
