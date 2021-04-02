from collections import OrderedDict
from homeassistant import loader as loader
from homeassistant.config import CONF_CORE as CONF_CORE, CONF_PACKAGES as CONF_PACKAGES, CORE_CONFIG_SCHEMA as CORE_CONFIG_SCHEMA, YAML_CONFIG_FILE as YAML_CONFIG_FILE, _format_config_error as _format_config_error, config_per_platform as config_per_platform, extract_domain_configs as extract_domain_configs, load_yaml_config_file as load_yaml_config_file, merge_packages_config as merge_packages_config
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.requirements import RequirementsNotFound as RequirementsNotFound, async_get_integration_with_requirements as async_get_integration_with_requirements
from typing import Any, NamedTuple

class CheckConfigError(NamedTuple):
    message: str
    domain: Union[str, None]
    config: Union[ConfigType, None]

class HomeAssistantConfig(OrderedDict):
    errors: Any = ...
    def __init__(self) -> None: ...
    def add_error(self, message: str, domain: Union[str, None]=..., config: Union[ConfigType, None]=...) -> HomeAssistantConfig: ...
    @property
    def error_str(self) -> str: ...

async def async_check_ha_config_file(hass: HomeAssistant) -> HomeAssistantConfig: ...
