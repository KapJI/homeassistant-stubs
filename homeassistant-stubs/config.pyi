from homeassistant import auth as auth
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, ATTR_HIDDEN as ATTR_HIDDEN, CONF_ALLOWLIST_EXTERNAL_DIRS as CONF_ALLOWLIST_EXTERNAL_DIRS, CONF_ALLOWLIST_EXTERNAL_URLS as CONF_ALLOWLIST_EXTERNAL_URLS, CONF_AUTH_MFA_MODULES as CONF_AUTH_MFA_MODULES, CONF_AUTH_PROVIDERS as CONF_AUTH_PROVIDERS, CONF_CUSTOMIZE as CONF_CUSTOMIZE, CONF_CUSTOMIZE_DOMAIN as CONF_CUSTOMIZE_DOMAIN, CONF_CUSTOMIZE_GLOB as CONF_CUSTOMIZE_GLOB, CONF_ELEVATION as CONF_ELEVATION, CONF_EXTERNAL_URL as CONF_EXTERNAL_URL, CONF_ID as CONF_ID, CONF_INTERNAL_URL as CONF_INTERNAL_URL, CONF_LATITUDE as CONF_LATITUDE, CONF_LEGACY_TEMPLATES as CONF_LEGACY_TEMPLATES, CONF_LONGITUDE as CONF_LONGITUDE, CONF_MEDIA_DIRS as CONF_MEDIA_DIRS, CONF_NAME as CONF_NAME, CONF_PACKAGES as CONF_PACKAGES, CONF_TEMPERATURE_UNIT as CONF_TEMPERATURE_UNIT, CONF_TIME_ZONE as CONF_TIME_ZONE, CONF_TYPE as CONF_TYPE, CONF_UNIT_SYSTEM as CONF_UNIT_SYSTEM, CONF_UNIT_SYSTEM_IMPERIAL as CONF_UNIT_SYSTEM_IMPERIAL, LEGACY_CONF_WHITELIST_EXTERNAL_DIRS as LEGACY_CONF_WHITELIST_EXTERNAL_DIRS, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, SOURCE_YAML as SOURCE_YAML, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform, extract_domain_configs as extract_domain_configs
from homeassistant.helpers.entity_values import EntityValues as EntityValues
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import Integration as Integration, IntegrationNotFound as IntegrationNotFound
from homeassistant.requirements import RequirementsNotFound as RequirementsNotFound, async_get_integration_with_requirements as async_get_integration_with_requirements
from homeassistant.util.package import is_docker_env as is_docker_env
from homeassistant.util.unit_system import IMPERIAL_SYSTEM as IMPERIAL_SYSTEM, METRIC_SYSTEM as METRIC_SYSTEM
from homeassistant.util.yaml import SECRET_YAML as SECRET_YAML, Secrets as Secrets, load_yaml as load_yaml
from typing import Any, Callable

DATA_PERSISTENT_ERRORS: str
RE_YAML_ERROR: Any
RE_ASCII: Any
YAML_CONFIG_FILE: str
VERSION_FILE: str
CONFIG_DIR_NAME: str
DATA_CUSTOMIZE: str
GROUP_CONFIG_PATH: str
AUTOMATION_CONFIG_PATH: str
SCRIPT_CONFIG_PATH: str
SCENE_CONFIG_PATH: str
LOAD_EXCEPTIONS: Any
INTEGRATION_LOAD_EXCEPTIONS: Any
DEFAULT_CONFIG: Any
DEFAULT_SECRETS: str
TTS_PRE_92: str
TTS_92: str
PACKAGES_CONFIG_SCHEMA: Any
CUSTOMIZE_DICT_SCHEMA: Any
CUSTOMIZE_CONFIG_SCHEMA: Any
CORE_CONFIG_SCHEMA: Any

def get_default_config_dir() -> str: ...
async def async_ensure_config_exists(hass: HomeAssistant) -> bool: ...
async def async_create_default_config(hass: HomeAssistant) -> bool: ...
async def async_hass_config_yaml(hass: HomeAssistant) -> dict: ...
def load_yaml_config_file(config_path: str, secrets: Union[Secrets, None]=...) -> dict[Any, Any]: ...
def process_ha_config_upgrade(hass: HomeAssistant) -> None: ...
def async_log_exception(ex: Exception, domain: str, config: dict, hass: HomeAssistant, link: Union[str, None]=...) -> None: ...
async def async_process_ha_core_config(hass: HomeAssistant, config: dict) -> None: ...
async def merge_packages_config(hass: HomeAssistant, config: dict, packages: dict[str, Any], _log_pkg_error: Callable=...) -> dict: ...
async def async_process_component_config(hass: HomeAssistant, config: ConfigType, integration: Integration) -> Union[ConfigType, None]: ...
def config_without_domain(config: dict, domain: str) -> dict: ...
async def async_check_ha_config_file(hass: HomeAssistant) -> Union[str, None]: ...
def async_notify_setup_error(hass: HomeAssistant, component: str, display_link: Union[str, None]=...) -> None: ...
