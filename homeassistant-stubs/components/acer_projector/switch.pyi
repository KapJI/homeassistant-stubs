from .const import CMD_DICT as CMD_DICT, CONF_READ_TIMEOUT as CONF_READ_TIMEOUT, CONF_WRITE_TIMEOUT as CONF_WRITE_TIMEOUT, DEFAULT_NAME as DEFAULT_NAME, DEFAULT_READ_TIMEOUT as DEFAULT_READ_TIMEOUT, DEFAULT_WRITE_TIMEOUT as DEFAULT_WRITE_TIMEOUT, ECO_MODE as ECO_MODE, ICON as ICON, INPUT_SOURCE as INPUT_SOURCE, LAMP as LAMP, LAMP_HOURS as LAMP_HOURS
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_FILENAME as CONF_FILENAME, CONF_NAME as CONF_NAME, STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

def setup_platform(hass: HomeAssistant, config: ConfigType, add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class AcerSwitch(SwitchEntity):
    _attr_icon = ICON
    _serial_port: Incomplete
    _read_timeout: Incomplete
    _write_timeout: Incomplete
    _attr_name: Incomplete
    _attributes: Incomplete
    def __init__(self, serial_port: str, name: str, read_timeout: int, write_timeout: int) -> None: ...
    def _write_read(self, msg: str) -> str: ...
    def _write_read_format(self, msg: str) -> str: ...
    _attr_is_on: bool
    _attr_available: bool
    _attr_extra_state_attributes: Incomplete
    def update(self) -> None: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
