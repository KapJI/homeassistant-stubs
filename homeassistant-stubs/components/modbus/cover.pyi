from . import get_hub as get_hub
from .base_platform import BasePlatform as BasePlatform
from .const import CALL_TYPE_COIL as CALL_TYPE_COIL, CALL_TYPE_WRITE_COIL as CALL_TYPE_WRITE_COIL, CALL_TYPE_WRITE_REGISTER as CALL_TYPE_WRITE_REGISTER, CONF_STATE_CLOSED as CONF_STATE_CLOSED, CONF_STATE_CLOSING as CONF_STATE_CLOSING, CONF_STATE_OPEN as CONF_STATE_OPEN, CONF_STATE_OPENING as CONF_STATE_OPENING, CONF_STATUS_REGISTER as CONF_STATUS_REGISTER, CONF_STATUS_REGISTER_TYPE as CONF_STATUS_REGISTER_TYPE
from .modbus import ModbusHub as ModbusHub
from datetime import datetime
from homeassistant.components.cover import CoverEntity as CoverEntity, SUPPORT_CLOSE as SUPPORT_CLOSE, SUPPORT_OPEN as SUPPORT_OPEN
from homeassistant.const import CONF_COVERS as CONF_COVERS, CONF_NAME as CONF_NAME, STATE_CLOSED as STATE_CLOSED, STATE_CLOSING as STATE_CLOSING, STATE_OPEN as STATE_OPEN, STATE_OPENING as STATE_OPENING, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

PARALLEL_UPDATES: int

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class ModbusCover(BasePlatform, CoverEntity, RestoreEntity):
    _state_closed: Any
    _state_closing: Any
    _state_open: Any
    _state_opening: Any
    _status_register: Any
    _status_register_type: Any
    _attr_supported_features: Any
    _attr_is_closed: bool
    _write_type: Any
    _write_address: Any
    _address: Any
    _input_type: Any
    def __init__(self, hub: ModbusHub, config: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_is_opening: Any
    _attr_is_closing: Any
    def _set_attr_state(self, value: Union[str, bool, int]) -> None: ...
    _attr_available: Any
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    _call_active: bool
    _lazy_errors: Any
    async def async_update(self, now: Union[datetime, None] = ...) -> None: ...
