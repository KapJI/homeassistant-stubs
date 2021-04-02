from .const import ATTR_COUNTER as ATTR_COUNTER, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES as DEVICE_CLASSES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Callable, Iterable
from xknx.devices import BinarySensor as XknxBinarySensor

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable[[Iterable[Entity]], None], discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXBinarySensor(KnxEntity, BinarySensorEntity):
    _device: Any
    def __init__(self, device: XknxBinarySensor) -> None: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def force_update(self) -> bool: ...
