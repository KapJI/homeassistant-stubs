from .const import ATTR_LAST_KNX_UPDATE as ATTR_LAST_KNX_UPDATE, ATTR_SOURCE as ATTR_SOURCE, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from collections.abc import Iterable
from homeassistant.components.sensor import DEVICE_CLASSES as DEVICE_CLASSES, SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.util import dt as dt
from typing import Any, Callable
from xknx.devices import Sensor as XknxSensor

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: Callable[[Iterable[Entity]], None], discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXSensor(KnxEntity, SensorEntity):
    _device: Any
    _unique_id: Any = ...
    def __init__(self, device: XknxSensor) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def force_update(self) -> bool: ...
