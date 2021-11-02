from . import get_hub as get_hub
from .base_platform import BasePlatform as BasePlatform
from datetime import datetime
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.const import CONF_BINARY_SENSORS as CONF_BINARY_SENSORS, CONF_NAME as CONF_NAME, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ModbusBinarySensor(BasePlatform, RestoreEntity, BinarySensorEntity):
    _attr_is_on: Any
    async def async_added_to_hass(self) -> None: ...
    _call_active: bool
    _lazy_errors: Any
    _attr_available: bool
    async def async_update(self, now: Union[datetime, None] = ...) -> None: ...
