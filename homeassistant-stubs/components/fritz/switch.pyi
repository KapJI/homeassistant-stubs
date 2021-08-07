from .common import FritzBoxBaseEntity as FritzBoxBaseEntity, FritzBoxTools as FritzBoxTools, FritzData as FritzData, FritzDevice as FritzDevice, FritzDeviceBase as FritzDeviceBase, SwitchInfo as SwitchInfo
from .const import DATA_FRITZ as DATA_FRITZ, DOMAIN as DOMAIN, SWITCH_TYPE_DEFLECTION as SWITCH_TYPE_DEFLECTION, SWITCH_TYPE_PORTFORWARD as SWITCH_TYPE_PORTFORWARD, SWITCH_TYPE_WIFINETWORK as SWITCH_TYPE_WIFINETWORK
from collections import OrderedDict
from homeassistant.components.network import async_get_source_ip as async_get_source_ip
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Any

async def async_service_call_action(fritzbox_tools: FritzBoxTools, service_name: str, service_suffix: Union[str, None], action_name: str, **kwargs: Any) -> Union[None, dict]: ...
def service_call_action(fritzbox_tools: FritzBoxTools, service_name: str, service_suffix: Union[str, None], action_name: str, **kwargs: Any) -> Union[dict, None]: ...
def get_deflections(fritzbox_tools: FritzBoxTools, service_name: str) -> Union[list[OrderedDict[Any, Any]], None]: ...
def deflection_entities_list(fritzbox_tools: FritzBoxTools, device_friendly_name: str) -> list[FritzBoxDeflectionSwitch]: ...
def port_entities_list(fritzbox_tools: FritzBoxTools, device_friendly_name: str, local_ip: str) -> list[FritzBoxPortSwitch]: ...
def wifi_entities_list(fritzbox_tools: FritzBoxTools, device_friendly_name: str) -> list[FritzBoxWifiSwitch]: ...
def profile_entities_list(router: FritzBoxTools, data_fritz: FritzData) -> list[FritzBoxProfileSwitch]: ...
def all_entities_list(fritzbox_tools: FritzBoxTools, device_friendly_name: str, data_fritz: FritzData, local_ip: str) -> list[Entity]: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxBaseSwitch(FritzBoxBaseEntity):
    _description: Any
    _friendly_name: Any
    _icon: Any
    _type: Any
    _update: Any
    _switch: Any
    _name: Any
    _unique_id: Any
    _attributes: Any
    _is_available: bool
    _attr_is_on: bool
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, switch_info: SwitchInfo) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def icon(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    async def async_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_handle_turn_on_off(self, turn_on: bool) -> bool: ...

class FritzBoxPortSwitch(FritzBoxBaseSwitch, SwitchEntity):
    _fritzbox_tools: Any
    _attributes: Any
    connection_type: Any
    port_mapping: Any
    _idx: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, port_mapping: Union[dict[str, Any], None], idx: int, connection_type: str) -> None: ...
    _is_available: bool
    _attr_is_on: Any
    async def _async_fetch_update(self) -> None: ...
    async def _async_handle_port_switch_on_off(self, turn_on: bool) -> bool: ...

class FritzBoxDeflectionSwitch(FritzBoxBaseSwitch, SwitchEntity):
    _fritzbox_tools: Any
    dict_of_deflection: Any
    _attributes: Any
    id: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, dict_of_deflection: Any) -> None: ...
    _is_available: bool
    _attr_is_on: Any
    async def _async_fetch_update(self) -> None: ...
    async def _async_switch_on_off_executor(self, turn_on: bool) -> None: ...

class FritzBoxProfileSwitch(FritzDeviceBase, SwitchEntity):
    _attr_icon: str
    _attr_is_on: bool
    _name: Any
    _attr_unique_id: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device: FritzDevice) -> None: ...
    async def async_process_update(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _async_handle_turn_on_off(self, turn_on: bool) -> bool: ...
    async def _async_switch_on_off(self, turn_on: bool) -> None: ...

class FritzBoxWifiSwitch(FritzBoxBaseSwitch, SwitchEntity):
    _fritzbox_tools: Any
    _attributes: Any
    _network_num: Any
    def __init__(self, fritzbox_tools: FritzBoxTools, device_friendly_name: str, network_num: int, network_name: str) -> None: ...
    _is_available: bool
    _attr_is_on: Any
    async def _async_fetch_update(self) -> None: ...
    async def _async_switch_on_off_executor(self, turn_on: bool) -> None: ...