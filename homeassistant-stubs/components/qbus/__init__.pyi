from .const import DOMAIN as DOMAIN, PLATFORMS as PLATFORMS
from .coordinator import QBUS_KEY as QBUS_KEY, QbusConfigCoordinator as QbusConfigCoordinator, QbusConfigEntry as QbusConfigEntry, QbusControllerCoordinator as QbusControllerCoordinator
from _typeshed import Incomplete
from homeassistant.components.mqtt import async_wait_for_mqtt_client as async_wait_for_mqtt_client
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers.typing import ConfigType as ConfigType

_LOGGER: Incomplete
CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: QbusConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: QbusConfigEntry) -> bool: ...
def _cleanup(hass: HomeAssistant, entry: QbusConfigEntry) -> None: ...
