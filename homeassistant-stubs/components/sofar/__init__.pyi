from .const import CONF_UNIT_ID as CONF_UNIT_ID, DOMAIN as DOMAIN, METER_ENERGY as METER_ENERGY, SCAN_INTERVAL as SCAN_INTERVAL, SETTINGS_SCAN_INTERVAL as SETTINGS_SCAN_INTERVAL
from .coordinator import SofarConfigEntry as SofarConfigEntry, SofarDataUpdateCoordinator as SofarDataUpdateCoordinator, SofarRuntimeData as SofarRuntimeData
from .sensor import SENSOR_DESCRIPTIONS as SENSOR_DESCRIPTIONS
from .services import async_setup_services as async_setup_services
from _typeshed import Incomplete
from homeassistant.components.modbus import async_get_unit as async_get_unit
from homeassistant.components.sensor import SensorExtraStoredData as SensorExtraStoredData
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError
from homeassistant.helpers import device_registry as dr, restore_state as restore_state
from homeassistant.helpers.typing import ConfigType as ConfigType
from sofar_modbus.modern.device import SofarInverter

_LOGGER: Incomplete
PLATFORMS: list[Platform]
_IDENTITY_ATTEMPTS: int
_REMOVED_SENSOR_KEYS: Incomplete
CONFIG_SCHEMA: Incomplete

@callback
def _async_remove_stale_sensors(hass: HomeAssistant, serial: str) -> None: ...
@callback
def _async_remove_denied_meter_energy(hass: HomeAssistant, serial: str, served: frozenset[str]) -> None: ...
async def _async_read_identity(entry: SofarConfigEntry, device: SofarInverter) -> None: ...
def _async_seed_high_water_marks(hass: HomeAssistant, serial: str, device: SofarInverter) -> None: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: SofarConfigEntry) -> bool: ...
def _battery_pack_number(serial: str, identifier: str) -> int | None: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: SofarConfigEntry, device_entry: dr.AnyDeviceEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: SofarConfigEntry) -> bool: ...
