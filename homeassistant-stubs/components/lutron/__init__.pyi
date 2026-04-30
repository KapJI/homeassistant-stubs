from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady
from homeassistant.helpers import device_registry as dr, entity_registry as er
from pylutron import Button as Button, Keypad as Keypad, Led as Led, Lutron, OccupancyGroup as OccupancyGroup, Output as Output

PLATFORMS: Incomplete
_LOGGER: Incomplete
ATTR_ACTION: str
ATTR_FULL_ID: str
ATTR_UUID: str
type LutronConfigEntry = ConfigEntry[LutronData]

@dataclass(slots=True, kw_only=True)
class LutronData:
    client: Lutron
    binary_sensors: list[tuple[str, OccupancyGroup]]
    buttons: list[tuple[str, Keypad, Button]]
    covers: list[tuple[str, Output]]
    fans: list[tuple[str, Output]]
    lights: list[tuple[str, Output]]
    scenes: list[tuple[str, Keypad, Button, Led | None]]
    switches: list[tuple[str, Output]]

async def async_setup_entry(hass: HomeAssistant, config_entry: LutronConfigEntry) -> bool: ...
def _setup_output(hass: HomeAssistant, entry_data: LutronData, output: Output, area_name: str, entity_registry: er.EntityRegistry, device_registry: dr.DeviceRegistry) -> None: ...
def _setup_keypad(hass: HomeAssistant, entry_data: LutronData, keypad: Keypad, area_name: str, entity_registry: er.EntityRegistry, device_registry: dr.DeviceRegistry) -> None: ...
def _async_check_entity_unique_id(hass: HomeAssistant, entity_registry: er.EntityRegistry, platform: str, uuid: str, legacy_uuid: str, controller_guid: str) -> None: ...
def _async_check_device_identifiers(hass: HomeAssistant, device_registry: dr.DeviceRegistry, uuid: str, legacy_uuid: str, controller_guid: str) -> None: ...
def _async_check_keypad_identifiers(hass: HomeAssistant, device_registry: dr.DeviceRegistry, keypad_id: int, uuid: str, legacy_uuid: str, controller_guid: str) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: LutronConfigEntry) -> bool: ...
