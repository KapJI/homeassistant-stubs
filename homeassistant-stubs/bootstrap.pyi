from . import config_entries as config_entries, core as core, loader as loader
from .components import http as http
from .const import REQUIRED_NEXT_PYTHON_HA_RELEASE as REQUIRED_NEXT_PYTHON_HA_RELEASE, REQUIRED_NEXT_PYTHON_VER as REQUIRED_NEXT_PYTHON_VER, SIGNAL_BOOTSTRAP_INTEGRATIONS as SIGNAL_BOOTSTRAP_INTEGRATIONS
from .exceptions import HomeAssistantError as HomeAssistantError
from .helpers import area_registry as area_registry, device_registry as device_registry, entity_registry as entity_registry, issue_registry as issue_registry, recorder as recorder
from .helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from .helpers.typing import ConfigType as ConfigType
from .runner import RuntimeConfig as RuntimeConfig
from .setup import DATA_SETUP as DATA_SETUP, DATA_SETUP_STARTED as DATA_SETUP_STARTED, DATA_SETUP_TIME as DATA_SETUP_TIME, async_set_domains_to_be_loaded as async_set_domains_to_be_loaded, async_setup_component as async_setup_component
from .util.logging import async_activate_log_queue_handler as async_activate_log_queue_handler
from .util.package import async_get_user_site as async_get_user_site, is_virtual_env as is_virtual_env
from _typeshed import Incomplete
from typing import Any

_LOGGER: Incomplete
ERROR_LOG_FILENAME: str
DATA_LOGGING: str
DATA_REGISTRIES_LOADED: str
LOG_SLOW_STARTUP_INTERVAL: int
SLOW_STARTUP_CHECK_INTERVAL: int
STAGE_1_TIMEOUT: int
STAGE_2_TIMEOUT: int
WRAP_UP_TIMEOUT: int
COOLDOWN_TIME: int
MAX_LOAD_CONCURRENTLY: int
DEBUGGER_INTEGRATIONS: Incomplete
CORE_INTEGRATIONS: Incomplete
LOGGING_INTEGRATIONS: Incomplete
FRONTEND_INTEGRATIONS: Incomplete
RECORDER_INTEGRATIONS: Incomplete
DISCOVERY_INTEGRATIONS: Incomplete
STAGE_1_INTEGRATIONS: Incomplete

async def async_setup_hass(runtime_config: RuntimeConfig) -> Union[core.HomeAssistant, None]: ...
def open_hass_ui(hass: core.HomeAssistant) -> None: ...
async def load_registries(hass: core.HomeAssistant) -> None: ...
async def async_from_config_dict(config: ConfigType, hass: core.HomeAssistant) -> Union[core.HomeAssistant, None]: ...
def async_enable_logging(hass: core.HomeAssistant, verbose: bool = ..., log_rotate_days: Union[int, None] = ..., log_file: Union[str, None] = ..., log_no_color: bool = ...) -> None: ...
async def async_mount_local_lib_path(config_dir: str) -> str: ...
def _get_domains(hass: core.HomeAssistant, config: dict[str, Any]) -> set[str]: ...
async def _async_watch_pending_setups(hass: core.HomeAssistant) -> None: ...
async def async_setup_multi_components(hass: core.HomeAssistant, domains: set[str], config: dict[str, Any]) -> None: ...
async def _async_set_up_integrations(hass: core.HomeAssistant, config: dict[str, Any]) -> None: ...
