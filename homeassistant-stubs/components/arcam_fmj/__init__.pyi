from .const import DEFAULT_SCAN_INTERVAL as DEFAULT_SCAN_INTERVAL
from .coordinator import ArcamFmjConfigEntry as ArcamFmjConfigEntry, ArcamFmjCoordinator as ArcamFmjCoordinator, ArcamFmjRuntimeData as ArcamFmjRuntimeData
from _typeshed import Incomplete
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant

_LOGGER: Incomplete
PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ArcamFmjConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ArcamFmjConfigEntry) -> bool: ...
async def _run_client(hass: HomeAssistant, runtime_data: ArcamFmjRuntimeData, interval: float) -> None: ...
