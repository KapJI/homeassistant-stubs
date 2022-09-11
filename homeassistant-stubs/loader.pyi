import pathlib
from .core import HomeAssistant as HomeAssistant
from .generated.application_credentials import APPLICATION_CREDENTIALS as APPLICATION_CREDENTIALS
from .generated.bluetooth import BLUETOOTH as BLUETOOTH
from .generated.dhcp import DHCP as DHCP
from .generated.mqtt import MQTT as MQTT
from .generated.ssdp import SSDP as SSDP
from .generated.usb import USB as USB
from .generated.zeroconf import HOMEKIT as HOMEKIT, ZEROCONF as ZEROCONF
from .helpers.json import JSON_DECODE_EXCEPTIONS as JSON_DECODE_EXCEPTIONS, json_loads as json_loads
from _typeshed import Incomplete
from awesomeversion import AwesomeVersion
from collections.abc import Callable, Iterable
from types import ModuleType
from typing import Any, Literal, TypeVar, TypedDict

_CallableT = TypeVar('_CallableT', bound=Callable[..., Any])
_LOGGER: Incomplete
DATA_COMPONENTS: str
DATA_INTEGRATIONS: str
DATA_CUSTOM_COMPONENTS: str
PACKAGE_CUSTOM_COMPONENTS: str
PACKAGE_BUILTIN: str
CUSTOM_WARNING: str
_UNDEF: Incomplete
MAX_LOAD_CONCURRENTLY: int
MOVED_ZEROCONF_PROPS: Incomplete

class DHCPMatcherRequired(TypedDict):
    domain: str

class DHCPMatcherOptional(TypedDict):
    macaddress: str
    hostname: str
    registered_devices: bool

class DHCPMatcher(DHCPMatcherRequired, DHCPMatcherOptional): ...

class BluetoothMatcherRequired(TypedDict):
    domain: str

class BluetoothMatcherOptional(TypedDict):
    local_name: str
    service_uuid: str
    service_data_uuid: str
    manufacturer_id: int
    manufacturer_data_start: list[int]
    connectable: bool

class BluetoothMatcher(BluetoothMatcherRequired, BluetoothMatcherOptional): ...

class USBMatcherRequired(TypedDict):
    domain: str

class USBMatcherOptional(TypedDict):
    vid: str
    pid: str
    serial_number: str
    manufacturer: str
    description: str

class USBMatcher(USBMatcherRequired, USBMatcherOptional): ...

class Manifest(TypedDict):
    name: str
    disabled: str
    domain: str
    integration_type: Literal['integration', 'helper']
    dependencies: list[str]
    after_dependencies: list[str]
    requirements: list[str]
    config_flow: bool
    documentation: str
    issue_tracker: str
    quality_scale: str
    iot_class: str
    bluetooth: list[dict[str, Union[int, str]]]
    mqtt: list[str]
    ssdp: list[dict[str, str]]
    zeroconf: list[Union[str, dict[str, str]]]
    dhcp: list[dict[str, Union[bool, str]]]
    usb: list[dict[str, str]]
    homekit: dict[str, list[str]]
    is_built_in: bool
    version: str
    codeowners: list[str]
    loggers: list[str]
    supported_brands: dict[str, str]

def manifest_from_legacy_module(domain: str, module: ModuleType) -> Manifest: ...
async def _async_get_custom_components(hass: HomeAssistant) -> dict[str, Integration]: ...
async def async_get_custom_components(hass: HomeAssistant) -> dict[str, Integration]: ...
async def async_get_config_flows(hass: HomeAssistant, type_filter: Union[Literal['helper', 'integration'], None] = ...) -> set[str]: ...
async def async_get_application_credentials(hass: HomeAssistant) -> list[str]: ...
def async_process_zeroconf_match_dict(entry: dict[str, Any]) -> dict[str, Any]: ...
async def async_get_zeroconf(hass: HomeAssistant) -> dict[str, list[dict[str, Union[str, dict[str, str]]]]]: ...
async def async_get_bluetooth(hass: HomeAssistant) -> list[BluetoothMatcher]: ...
async def async_get_dhcp(hass: HomeAssistant) -> list[DHCPMatcher]: ...
async def async_get_usb(hass: HomeAssistant) -> list[USBMatcher]: ...
async def async_get_homekit(hass: HomeAssistant) -> dict[str, str]: ...
async def async_get_ssdp(hass: HomeAssistant) -> dict[str, list[dict[str, str]]]: ...
async def async_get_mqtt(hass: HomeAssistant) -> dict[str, list[str]]: ...

class Integration:
    @classmethod
    def resolve_from_root(cls, hass: HomeAssistant, root_module: ModuleType, domain: str) -> Union[Integration, None]: ...
    hass: Incomplete
    pkg_path: Incomplete
    file_path: Incomplete
    manifest: Incomplete
    _all_dependencies_resolved: Incomplete
    _all_dependencies: Incomplete
    def __init__(self, hass: HomeAssistant, pkg_path: str, file_path: pathlib.Path, manifest: Manifest) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def disabled(self) -> Union[str, None]: ...
    @property
    def domain(self) -> str: ...
    @property
    def dependencies(self) -> list[str]: ...
    @property
    def after_dependencies(self) -> list[str]: ...
    @property
    def requirements(self) -> list[str]: ...
    @property
    def config_flow(self) -> bool: ...
    @property
    def documentation(self) -> Union[str, None]: ...
    @property
    def issue_tracker(self) -> Union[str, None]: ...
    @property
    def loggers(self) -> Union[list[str], None]: ...
    @property
    def quality_scale(self) -> Union[str, None]: ...
    @property
    def iot_class(self) -> Union[str, None]: ...
    @property
    def integration_type(self) -> Literal['integration', 'helper']: ...
    @property
    def mqtt(self) -> Union[list[str], None]: ...
    @property
    def ssdp(self) -> Union[list[dict[str, str]], None]: ...
    @property
    def zeroconf(self) -> Union[list[Union[str, dict[str, str]]], None]: ...
    @property
    def bluetooth(self) -> Union[list[dict[str, Union[str, int]]], None]: ...
    @property
    def dhcp(self) -> Union[list[dict[str, Union[str, bool]]], None]: ...
    @property
    def usb(self) -> Union[list[dict[str, str]], None]: ...
    @property
    def homekit(self) -> Union[dict[str, list[str]], None]: ...
    @property
    def is_built_in(self) -> bool: ...
    @property
    def version(self) -> Union[AwesomeVersion, None]: ...
    @property
    def all_dependencies(self) -> set[str]: ...
    @property
    def all_dependencies_resolved(self) -> bool: ...
    async def resolve_dependencies(self) -> bool: ...
    def get_component(self) -> ModuleType: ...
    def get_platform(self, platform_name: str) -> ModuleType: ...
    def _import_platform(self, platform_name: str) -> ModuleType: ...
    def __repr__(self) -> str: ...

def _resolve_integrations_from_root(hass: HomeAssistant, root_module: ModuleType, domains: list[str]) -> dict[str, Integration]: ...
async def async_get_integration(hass: HomeAssistant, domain: str) -> Integration: ...
async def async_get_integrations(hass: HomeAssistant, domains: Iterable[str]) -> dict[str, Union[Integration, Exception]]: ...

class LoaderError(Exception): ...

class IntegrationNotFound(LoaderError):
    domain: Incomplete
    def __init__(self, domain: str) -> None: ...

class CircularDependency(LoaderError):
    from_domain: Incomplete
    to_domain: Incomplete
    def __init__(self, from_domain: str, to_domain: str) -> None: ...

def _load_file(hass: HomeAssistant, comp_or_platform: str, base_paths: list[str]) -> Union[ModuleType, None]: ...

class ModuleWrapper:
    _hass: Incomplete
    _module: Incomplete
    def __init__(self, hass: HomeAssistant, module: ModuleType) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...

class Components:
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, comp_name: str) -> ModuleWrapper: ...

class Helpers:
    _hass: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def __getattr__(self, helper_name: str) -> ModuleWrapper: ...

def bind_hass(func: _CallableT) -> _CallableT: ...
async def _async_component_dependencies(hass: HomeAssistant, start_domain: str, integration: Integration, loaded: set[str], loading: set[str]) -> set[str]: ...
def _async_mount_config_dir(hass: HomeAssistant) -> bool: ...
def _lookup_path(hass: HomeAssistant) -> list[str]: ...
