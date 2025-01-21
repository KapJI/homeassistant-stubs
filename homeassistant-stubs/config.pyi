import voluptuous as vol
from .const import CONF_PACKAGES as CONF_PACKAGES, CONF_PLATFORM as CONF_PLATFORM, __version__ as __version__
from .core import HomeAssistant as HomeAssistant, callback as callback
from .core_config import _PACKAGES_CONFIG_SCHEMA as _PACKAGES_CONFIG_SCHEMA, _PACKAGE_DEFINITION_SCHEMA as _PACKAGE_DEFINITION_SCHEMA
from .exceptions import ConfigValidationError as ConfigValidationError, HomeAssistantError as HomeAssistantError
from .helpers.translation import async_get_exception_message as async_get_exception_message
from .helpers.typing import ConfigType as ConfigType
from .loader import ComponentProtocol as ComponentProtocol, Integration as Integration, IntegrationNotFound as IntegrationNotFound
from .requirements import RequirementsNotFound as RequirementsNotFound, async_get_integration_with_requirements as async_get_integration_with_requirements
from .util.async_ import create_eager_task as create_eager_task
from .util.package import is_docker_env as is_docker_env
from .util.yaml import SECRET_YAML as SECRET_YAML, Secrets as Secrets, YamlTypeError as YamlTypeError, load_yaml_dict as load_yaml_dict
from .util.yaml.objects import NodeStrClass as NodeStrClass
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Hashable, Iterable, Sequence
from dataclasses import dataclass
from enum import StrEnum
from typing import Any

_LOGGER: Incomplete
RE_YAML_ERROR: Incomplete
RE_ASCII: Incomplete
YAML_CONFIG_FILE: str
VERSION_FILE: str
CONFIG_DIR_NAME: str
AUTOMATION_CONFIG_PATH: str
SCRIPT_CONFIG_PATH: str
SCENE_CONFIG_PATH: str
LOAD_EXCEPTIONS: Incomplete
INTEGRATION_LOAD_EXCEPTIONS: Incomplete
SAFE_MODE_FILENAME: str
DEFAULT_CONFIG: Incomplete
DEFAULT_SECRETS: str
TTS_PRE_92: str
TTS_92: str

class ConfigErrorTranslationKey(StrEnum):
    CONFIG_VALIDATION_ERR = 'config_validation_err'
    PLATFORM_CONFIG_VALIDATION_ERR = 'platform_config_validation_err'
    COMPONENT_IMPORT_ERR = 'component_import_err'
    CONFIG_PLATFORM_IMPORT_ERR = 'config_platform_import_err'
    CONFIG_VALIDATOR_UNKNOWN_ERR = 'config_validator_unknown_err'
    CONFIG_SCHEMA_UNKNOWN_ERR = 'config_schema_unknown_err'
    PLATFORM_COMPONENT_LOAD_ERR = 'platform_component_load_err'
    PLATFORM_COMPONENT_LOAD_EXC = 'platform_component_load_exc'
    PLATFORM_SCHEMA_VALIDATOR_ERR = 'platform_schema_validator_err'
    MULTIPLE_INTEGRATION_CONFIG_ERRORS = 'multiple_integration_config_errors'

_CONFIG_LOG_SHOW_STACK_TRACE: dict[ConfigErrorTranslationKey, bool]

@dataclass
class ConfigExceptionInfo:
    exception: Exception
    translation_key: ConfigErrorTranslationKey
    platform_path: str
    config: ConfigType
    integration_link: str | None

@dataclass
class IntegrationConfigInfo:
    config: ConfigType | None
    exception_info_list: list[ConfigExceptionInfo]

def get_default_config_dir() -> str: ...
async def async_ensure_config_exists(hass: HomeAssistant) -> bool: ...
async def async_create_default_config(hass: HomeAssistant) -> bool: ...
def _write_default_config(config_dir: str) -> bool: ...
async def async_hass_config_yaml(hass: HomeAssistant) -> dict: ...
def load_yaml_config_file(config_path: str, secrets: Secrets | None = None) -> dict[Any, Any]: ...
def process_ha_config_upgrade(hass: HomeAssistant) -> None: ...
@callback
def async_log_schema_error(exc: vol.Invalid, domain: str, config: dict, hass: HomeAssistant, link: str | None = None) -> None: ...
@callback
def async_log_config_validator_error(exc: vol.Invalid | HomeAssistantError, domain: str, config: dict, hass: HomeAssistant, link: str | None = None) -> None: ...
def _get_annotation(item: Any) -> tuple[str, int | str] | None: ...
def _get_by_path(data: dict | list, items: list[Hashable]) -> Any: ...
def find_annotation(config: dict | list, path: list[Hashable]) -> tuple[str, int | str] | None: ...
def _relpath(hass: HomeAssistant, path: str) -> str: ...
def stringify_invalid(hass: HomeAssistant, exc: vol.Invalid, domain: str, config: dict, link: str | None, max_sub_error_length: int) -> str: ...
def humanize_error(hass: HomeAssistant, validation_error: vol.Invalid, domain: str, config: dict, link: str | None, max_sub_error_length: int = ...) -> str: ...
@callback
def format_homeassistant_error(hass: HomeAssistant, exc: HomeAssistantError, domain: str, config: dict, link: str | None = None) -> str: ...
@callback
def format_schema_error(hass: HomeAssistant, exc: vol.Invalid, domain: str, config: dict, link: str | None = None) -> str: ...
def _log_pkg_error(hass: HomeAssistant, package: str, component: str | None, config: dict, message: str) -> None: ...
def _identify_config_schema(module: ComponentProtocol) -> str | None: ...
def _validate_package_definition(name: str, conf: Any) -> None: ...
def _recursive_merge(conf: dict[str, Any], package: dict[str, Any]) -> str | None: ...
async def merge_packages_config(hass: HomeAssistant, config: dict, packages: dict[str, Any], _log_pkg_error: Callable[[HomeAssistant, str, str | None, dict, str], None] = ...) -> dict: ...
@callback
def _get_log_message_and_stack_print_pref(hass: HomeAssistant, domain: str, platform_exception: ConfigExceptionInfo) -> tuple[str | None, bool, dict[str, str]]: ...
async def async_process_component_and_handle_errors(hass: HomeAssistant, config: ConfigType, integration: Integration, raise_on_failure: bool = False) -> ConfigType | None: ...
@callback
def async_drop_config_annotations(integration_config_info: IntegrationConfigInfo, integration: Integration) -> ConfigType | None: ...
@callback
def async_handle_component_errors(hass: HomeAssistant, integration_config_info: IntegrationConfigInfo, integration: Integration, raise_on_failure: bool = False) -> None: ...
def config_per_platform(config: ConfigType, domain: str) -> Iterable[tuple[str | None, ConfigType]]: ...
def extract_platform_integrations(config: ConfigType, domains: set[str]) -> dict[str, set[str]]: ...
def extract_domain_configs(config: ConfigType, domain: str) -> Sequence[str]: ...

@dataclass(slots=True)
class _PlatformIntegration:
    path: str
    name: str
    integration: Integration
    config: ConfigType
    validated_config: ConfigType

async def _async_load_and_validate_platform_integration(domain: str, integration_docs: str | None, config_exceptions: list[ConfigExceptionInfo], p_integration: _PlatformIntegration) -> ConfigType | None: ...
async def async_process_component_config(hass: HomeAssistant, config: ConfigType, integration: Integration, component: ComponentProtocol | None = None) -> IntegrationConfigInfo: ...
@callback
def config_without_domain(config: ConfigType, domain: str) -> ConfigType: ...
async def async_check_ha_config_file(hass: HomeAssistant) -> str | None: ...
def safe_mode_enabled(config_dir: str) -> bool: ...
async def async_enable_safe_mode(hass: HomeAssistant) -> None: ...
