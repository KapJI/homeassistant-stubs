from .const import DOMAIN as DOMAIN, LOGGER as LOGGER, NOTIFICATION_ID as NOTIFICATION_ID, NOTIFICATION_TITLE as NOTIFICATION_TITLE, SCAN_INTERVAL as SCAN_INTERVAL
from .coordinator import HydrawiseDataUpdateCoordinator as HydrawiseDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components import persistent_notification as persistent_notification
from homeassistant.const import CONF_ACCESS_TOKEN as CONF_ACCESS_TOKEN, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.typing import ConfigType as ConfigType

CONFIG_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
def _show_failure_notification(hass: HomeAssistant, error: str) -> None: ...
