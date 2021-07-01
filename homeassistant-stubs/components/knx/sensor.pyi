from .const import ATTR_LAST_KNX_UPDATE as ATTR_LAST_KNX_UPDATE, ATTR_SOURCE as ATTR_SOURCE, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from .schema import SensorSchema as SensorSchema
from homeassistant.components.sensor import DEVICE_CLASSES as DEVICE_CLASSES, SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType, StateType as StateType
from homeassistant.util import dt as dt
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Sensor as XknxSensor

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
def _create_sensor(xknx: XKNX, config: ConfigType) -> XknxSensor: ...

class KNXSensor(KnxEntity, SensorEntity):
    _device: XknxSensor
    _attr_device_class: Any
    _attr_force_update: Any
    _attr_unique_id: Any
    _attr_unit_of_measurement: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def state(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
