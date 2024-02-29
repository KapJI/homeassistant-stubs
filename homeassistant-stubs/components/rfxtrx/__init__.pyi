import RFXtrx as rfxtrxmod
from .const import ATTR_EVENT as ATTR_EVENT, COMMAND_GROUP_LIST as COMMAND_GROUP_LIST, CONF_AUTOMATIC_ADD as CONF_AUTOMATIC_ADD, CONF_DATA_BITS as CONF_DATA_BITS, CONF_PROTOCOLS as CONF_PROTOCOLS, DATA_RFXOBJECT as DATA_RFXOBJECT, DEVICE_PACKET_TYPE_LIGHTING4 as DEVICE_PACKET_TYPE_LIGHTING4, DOMAIN as DOMAIN, EVENT_RFXTRX_EVENT as EVENT_RFXTRX_EVENT, SERVICE_SEND as SERVICE_SEND
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID, CONF_DEVICE as CONF_DEVICE, CONF_DEVICES as CONF_DEVICES, CONF_DEVICE_ID as CONF_DEVICE_ID, CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect, async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any, NamedTuple, TypeVarTuple

DEFAULT_OFF_DELAY: float
SIGNAL_EVENT: Incomplete
CONNECT_TIMEOUT: float
_Ts = TypeVarTuple('_Ts')
_LOGGER: Incomplete

class DeviceTuple(NamedTuple):
    packettype: str
    subtype: str
    id_string: str

def _bytearray_string(data: Any) -> bytearray: ...

SERVICE_SEND_SCHEMA: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
def _create_rfx(config: Mapping[str, Any], event_callback: Callable[[rfxtrxmod.RFXtrxEvent], None]) -> rfxtrxmod.Connect: ...
def _get_device_lookup(devices: dict[str, dict[str, Any]]) -> dict[DeviceTuple, dict[str, Any]]: ...
async def async_setup_internal(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
async def async_setup_platform_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, supported: Callable[[rfxtrxmod.RFXtrxEvent], bool], constructor: Callable[[rfxtrxmod.RFXtrxEvent, rfxtrxmod.RFXtrxEvent | None, DeviceTuple, dict[str, Any]], list[Entity]]) -> None: ...
def get_rfx_object(packetid: str) -> rfxtrxmod.RFXtrxEvent | None: ...
def get_pt2262_deviceid(device_id: str, nb_data_bits: int | None) -> bytes | None: ...
def get_pt2262_cmd(device_id: str, data_bits: int) -> str | None: ...
def get_device_data_bits(device: rfxtrxmod.RFXtrxDevice, devices: dict[DeviceTuple, dict[str, Any]]) -> int | None: ...
def find_possible_pt2262_device(device_ids: set[str], device_id: str) -> str | None: ...
def get_device_id(device: rfxtrxmod.RFXtrxDevice, data_bits: int | None = None) -> DeviceTuple: ...
def get_device_tuple_from_identifiers(identifiers: set[tuple[str, str]]) -> DeviceTuple | None: ...
def get_identifiers_from_device_tuple(device_tuple: DeviceTuple) -> set[tuple[str, str]]: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: ConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...

class RfxtrxEntity(RestoreEntity):
    _attr_assumed_state: bool
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _device: rfxtrxmod.RFXtrxDevice
    _event: rfxtrxmod.RFXtrxEvent | None
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    _device_id: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, event: rfxtrxmod.RFXtrxEvent | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    def _event_applies(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> bool: ...
    def _apply_event(self, event: rfxtrxmod.RFXtrxEvent) -> None: ...
    def _handle_event(self, event: rfxtrxmod.RFXtrxEvent, device_id: DeviceTuple) -> None: ...

class RfxtrxCommandEntity(RfxtrxEntity):
    _attr_name: Incomplete
    def __init__(self, device: rfxtrxmod.RFXtrxDevice, device_id: DeviceTuple, event: rfxtrxmod.RFXtrxEvent | None = None) -> None: ...
    async def _async_send(self, fun: Callable[[rfxtrxmod.PySerialTransport, Unpack[_Ts]], None], *args: Unpack[_Ts]) -> None: ...
