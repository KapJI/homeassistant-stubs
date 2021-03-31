from homeassistant.const import SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers import config_per_platform as config_per_platform
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform, async_get_platforms as async_get_platforms
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_integration as async_get_integration
from homeassistant.setup import async_setup_component as async_setup_component
from typing import Iterable

async def async_reload_integration_platforms(hass: HomeAssistant, integration_name: str, integration_platforms: Iterable) -> None: ...
async def async_integration_yaml_config(hass: HomeAssistant, integration_name: str) -> Union[ConfigType, None]: ...
def async_get_platform_without_config_entry(hass: HomeAssistant, integration_name: str, integration_platform_name: str) -> Union[EntityPlatform, None]: ...
async def async_setup_reload_service(hass: HomeAssistant, domain: str, platforms: Iterable) -> None: ...
def setup_reload_service(hass: HomeAssistant, domain: str, platforms: Iterable) -> None: ...
