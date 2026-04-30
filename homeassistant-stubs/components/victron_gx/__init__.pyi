from .hub import Hub as Hub, VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers import device_registry as dr

_LOGGER: Incomplete
PLATFORMS: list[Platform]

async def async_setup_entry(hass: HomeAssistant, entry: VictronGxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VictronGxConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: VictronGxConfigEntry, device_entry: dr.DeviceEntry) -> bool: ...
