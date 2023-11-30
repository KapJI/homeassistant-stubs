import abc
from .const import CONF_DNSMASQ as CONF_DNSMASQ, CONF_INTERFACE as CONF_INTERFACE, CONF_REQUIRE_IP as CONF_REQUIRE_IP, CONF_SSH_KEY as CONF_SSH_KEY, DEFAULT_DNSMASQ as DEFAULT_DNSMASQ, DEFAULT_INTERFACE as DEFAULT_INTERFACE, KEY_METHOD as KEY_METHOD, KEY_SENSORS as KEY_SENSORS, PROTOCOL_HTTP as PROTOCOL_HTTP, PROTOCOL_HTTPS as PROTOCOL_HTTPS, PROTOCOL_TELNET as PROTOCOL_TELNET, SENSORS_BYTES as SENSORS_BYTES, SENSORS_LOAD_AVG as SENSORS_LOAD_AVG, SENSORS_RATES as SENSORS_RATES, SENSORS_TEMPERATURES as SENSORS_TEMPERATURES
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from aioasuswrt.asuswrt import AsusWrt as AsusWrtLegacy
from aiohttp import ClientSession as ClientSession
from collections.abc import Callable, Coroutine
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODE as CONF_MODE, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_PROTOCOL as CONF_PROTOCOL, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.update_coordinator import UpdateFailed as UpdateFailed
from pyasuswrt import AsusWrtHttp
from typing import Any, NamedTuple, TypeVar

SENSORS_TYPE_BYTES: str
SENSORS_TYPE_COUNT: str
SENSORS_TYPE_LOAD_AVG: str
SENSORS_TYPE_RATES: str
SENSORS_TYPE_TEMPERATURES: str

class WrtDevice(NamedTuple):
    ip: Incomplete
    name: Incomplete
    connected_to: Incomplete

_LOGGER: Incomplete
_AsusWrtBridgeT = TypeVar('_AsusWrtBridgeT', bound='AsusWrtBridge')
_FuncType: Incomplete
_ReturnFuncType = Callable[[_AsusWrtBridgeT], Coroutine[Any, Any, dict[str, Any]]]

def handle_errors_and_zip(exceptions: type[Exception] | tuple[type[Exception], ...], keys: list[str] | None) -> Callable[[_FuncType], _ReturnFuncType]: ...

class AsusWrtBridge(ABC, metaclass=abc.ABCMeta):
    @staticmethod
    def get_bridge(hass: HomeAssistant, conf: dict[str, Any], options: dict[str, Any] | None = ...) -> AsusWrtBridge: ...
    _host: Incomplete
    _firmware: Incomplete
    _label_mac: Incomplete
    _model: Incomplete
    def __init__(self, host: str) -> None: ...
    @property
    def host(self) -> str: ...
    @property
    def firmware(self) -> str | None: ...
    @property
    def label_mac(self) -> str | None: ...
    @property
    def model(self) -> str | None: ...
    @property
    @abstractmethod
    def is_connected(self) -> bool: ...
    @abstractmethod
    async def async_connect(self) -> None: ...
    @abstractmethod
    async def async_disconnect(self) -> None: ...
    @abstractmethod
    async def async_get_connected_devices(self) -> dict[str, WrtDevice]: ...
    @abstractmethod
    async def async_get_available_sensors(self) -> dict[str, dict[str, Any]]: ...

class AsusWrtLegacyBridge(AsusWrtBridge):
    _protocol: Incomplete
    _api: Incomplete
    def __init__(self, conf: dict[str, Any], options: dict[str, Any] | None = ...) -> None: ...
    @staticmethod
    def _get_api(conf: dict[str, Any], options: dict[str, Any] | None = ...) -> AsusWrtLegacy: ...
    @property
    def is_connected(self) -> bool: ...
    async def async_connect(self) -> None: ...
    async def async_disconnect(self) -> None: ...
    async def async_get_connected_devices(self) -> dict[str, WrtDevice]: ...
    async def _get_nvram_info(self, info_type: str) -> dict[str, Any]: ...
    _label_mac: Incomplete
    async def _get_label_mac(self) -> None: ...
    _firmware: Incomplete
    async def _get_firmware(self) -> None: ...
    _model: Incomplete
    async def _get_model(self) -> None: ...
    async def async_get_available_sensors(self) -> dict[str, dict[str, Any]]: ...
    async def _get_available_temperature_sensors(self) -> list[str]: ...
    async def _get_bytes(self) -> Any: ...
    async def _get_rates(self) -> Any: ...
    async def _get_load_avg(self) -> Any: ...
    async def _get_temperatures(self) -> Any: ...

class AsusWrtHttpBridge(AsusWrtBridge):
    _api: Incomplete
    def __init__(self, conf: dict[str, Any], session: ClientSession) -> None: ...
    @staticmethod
    def _get_api(conf: dict[str, Any], session: ClientSession) -> AsusWrtHttp: ...
    @property
    def is_connected(self) -> bool: ...
    _label_mac: Incomplete
    _firmware: Incomplete
    _model: Incomplete
    async def async_connect(self) -> None: ...
    async def async_disconnect(self) -> None: ...
    async def async_get_connected_devices(self) -> dict[str, WrtDevice]: ...
    async def async_get_available_sensors(self) -> dict[str, dict[str, Any]]: ...
    async def _get_available_temperature_sensors(self) -> list[str]: ...
    async def _get_bytes(self) -> Any: ...
    async def _get_rates(self) -> Any: ...
    async def _get_load_avg(self) -> Any: ...
    async def _get_temperatures(self) -> Any: ...
