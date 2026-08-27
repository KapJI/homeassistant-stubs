from .const import DOMAIN as DOMAIN
from .hub import Hub as Hub, VictronGxConfigEntry as VictronGxConfigEntry
from _typeshed import Incomplete
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP, Platform as Platform
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as dr, start as start

_LOGGER: Incomplete
_LEGACY_EVCHARGER_SENSOR_SUFFIXES: Incomplete
_LEGACY_SENSOR_BREAKS_IN_VERSION: str
PLATFORMS: list[Platform]

def _automations_and_scripts_using_entity(hass: HomeAssistant, entity_id: str) -> list[str]: ...
def _async_check_legacy_sensors(hass: HomeAssistant, config_entry: VictronGxConfigEntry) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: VictronGxConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: VictronGxConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: VictronGxConfigEntry, device_entry: dr.AnyDeviceEntry) -> bool: ...
