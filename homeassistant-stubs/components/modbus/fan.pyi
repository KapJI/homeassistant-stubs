from . import get_hub as get_hub
from .base_platform import BaseSwitch as BaseSwitch
from .const import CONF_FANS as CONF_FANS
from .modbus import ModbusHub as ModbusHub
from homeassistant.components.fan import FanEntity as FanEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ModbusFan(BaseSwitch, FanEntity):
    async def async_turn_on(self, percentage: Union[int, None] = ..., preset_mode: Union[str, None] = ..., **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
