from .const import CONF_RESPOND_TO_READ as CONF_RESPOND_TO_READ, CONF_STATE_ADDRESS as CONF_STATE_ADDRESS, DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import NumberSchema as NumberSchema
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import NumericValue

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
def _create_numeric_value(xknx: XKNX, config: ConfigType) -> NumericValue: ...

class KNXNumber(KnxEntity, NumberEntity, RestoreEntity):
    _device: NumericValue
    _attr_max_value: Any
    _attr_min_value: Any
    _attr_step: Any
    _attr_unique_id: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def value(self) -> float: ...
    async def async_set_value(self, value: float) -> None: ...
