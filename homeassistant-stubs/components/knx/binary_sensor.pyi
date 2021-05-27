from .const import ATTR_COUNTER as ATTR_COUNTER, ATTR_LAST_KNX_UPDATE as ATTR_LAST_KNX_UPDATE, ATTR_SOURCE as ATTR_SOURCE, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from .schema import BinarySensorSchema as BinarySensorSchema
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import dt as dt
from typing import Any
from xknx import XKNX as XKNX

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXBinarySensor(KnxEntity, BinarySensorEntity):
    _device: Any
    _device_class: Any = ...
    _unique_id: Any = ...
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def force_update(self) -> bool: ...
