from .entity import WemoBinaryStateEntity as WemoBinaryStateEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, STATE_STANDBY as STATE_STANDBY, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import convert as convert
from typing import Any

SCAN_INTERVAL: Any
PARALLEL_UPDATES: int
ATTR_SENSOR_STATE: str
ATTR_SWITCH_MODE: str
ATTR_CURRENT_STATE_DETAIL: str
ATTR_COFFEMAKER_MODE: str
MAKER_SWITCH_MOMENTARY: str
MAKER_SWITCH_TOGGLE: str
WEMO_ON: int
WEMO_OFF: int
WEMO_STANDBY: int

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WemoSwitch(WemoBinaryStateEntity, SwitchEntity):
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @staticmethod
    def as_uptime(_seconds: int) -> str: ...
    @property
    def detail_state(self) -> str: ...
    @property
    def icon(self) -> Union[str, None]: ...
    def turn_on(self, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
