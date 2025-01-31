import types
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping, Sequence
from homeassistant.const import CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_NAME as CONF_NAME, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_set_service_schema as async_set_service_schema
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util import raise_if_invalid_filename as raise_if_invalid_filename
from homeassistant.util.yaml.loader import load_yaml_dict as load_yaml_dict
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
FOLDER: str
CONFIG_SCHEMA: Incomplete
ALLOWED_HASS: Incomplete
ALLOWED_EVENTBUS: Incomplete
ALLOWED_STATEMACHINE: Incomplete
ALLOWED_SERVICEREGISTRY: Incomplete
ALLOWED_TIME: Incomplete
ALLOWED_DATETIME: Incomplete
ALLOWED_DT_UTIL: Incomplete
CONF_FIELDS: str

class ScriptError(HomeAssistantError): ...

def setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def discover_scripts(hass: HomeAssistant) -> None: ...

IOPERATOR_TO_OPERATOR: Incomplete

def guarded_import(name: str, globals: Mapping[str, object] | None = None, locals: Mapping[str, object] | None = None, fromlist: Sequence[str] = (), level: int = 0) -> types.ModuleType: ...
def guarded_inplacevar(op: str, target: Any, operand: Any) -> Any: ...
@bind_hass
def execute_script(hass: HomeAssistant, name: str, data: dict[str, Any] | None = None, return_response: bool = False) -> dict | None: ...
@bind_hass
def execute(hass: HomeAssistant, filename: str, source: Any, data: dict[str, Any] | None = None, return_response: bool = False) -> dict | None: ...

class StubPrinter:
    def __init__(self, _getattr_: Callable) -> None: ...
    def _call_print(self, *objects: object, **kwargs: Any) -> None: ...

class TimeWrapper:
    warned: bool
    def sleep(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, attr: str) -> Any: ...
