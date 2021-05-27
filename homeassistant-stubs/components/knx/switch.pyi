from .const import DOMAIN as DOMAIN, KNX_ADDRESS as KNX_ADDRESS
from .knx_entity import KnxEntity as KnxEntity
from .schema import SwitchSchema as SwitchSchema
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any
from xknx import XKNX as XKNX

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None]=...) -> None: ...

class KNXSwitch(KnxEntity, SwitchEntity):
    _device: Any
    _unique_id: Any = ...
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
