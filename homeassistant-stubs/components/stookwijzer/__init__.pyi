from .const import DOMAIN as DOMAIN, LOGGER as LOGGER
from .coordinator import StookwijzerConfigEntry as StookwijzerConfigEntry, StookwijzerCoordinator as StookwijzerCoordinator
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.const import CONF_LATITUDE as CONF_LATITUDE, CONF_LOCATION as CONF_LOCATION, CONF_LONGITUDE as CONF_LONGITUDE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PLATFORMS: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: StookwijzerConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: StookwijzerConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: StookwijzerConfigEntry) -> bool: ...
@callback
def async_migrate_entity_entry(entity_entry: er.RegistryEntry) -> dict[str, Any] | None: ...
