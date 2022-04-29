import queue
from .base import FritzBoxPhonebook as FritzBoxPhonebook
from .const import ATTR_PREFIXES as ATTR_PREFIXES, CONF_PHONEBOOK as CONF_PHONEBOOK, CONF_PREFIXES as CONF_PREFIXES, DOMAIN as DOMAIN, FRITZBOX_PHONEBOOK as FRITZBOX_PHONEBOOK, FritzState as FritzState, ICON_PHONE as ICON_PHONE, MANUFACTURER as MANUFACTURER, SERIAL_NUMBER as SERIAL_NUMBER
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
SCAN_INTERVAL: Incomplete

class CallState(StrEnum):
    RINGING: str
    DIALING: str
    TALKING: str
    IDLE: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxCallSensor(SensorEntity):
    _attr_icon: Incomplete
    _fritzbox_phonebook: Incomplete
    _prefixes: Incomplete
    _host: Incomplete
    _port: Incomplete
    _monitor: Incomplete
    _attributes: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_native_value: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, name: str, unique_id: str, fritzbox_phonebook: FritzBoxPhonebook, prefixes: Union[list[str], None], host: str, port: int) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def _start_call_monitor(self) -> None: ...
    def _stop_call_monitor(self, event: Union[Event, None] = ...) -> None: ...
    def set_state(self, state: CallState) -> None: ...
    def set_attributes(self, attributes: Mapping[str, str]) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[str, list[str]]]: ...
    def number_to_name(self, number: str) -> str: ...
    def update(self) -> None: ...

class FritzBoxCallMonitor:
    host: Incomplete
    port: Incomplete
    connection: Incomplete
    stopped: Incomplete
    _sensor: Incomplete
    def __init__(self, host: str, port: int, sensor: FritzBoxCallSensor) -> None: ...
    def connect(self) -> None: ...
    def _process_events(self, event_queue: queue.Queue[str]) -> None: ...
    def _parse(self, event: str) -> None: ...
