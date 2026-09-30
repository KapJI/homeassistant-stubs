from .const import ATTACHMENT_SCAN_INTERVAL as ATTACHMENT_SCAN_INTERVAL, CONF_UNIT_ID as CONF_UNIT_ID, DOMAIN as DOMAIN, LOGGER as LOGGER, SCAN_INTERVAL as SCAN_INTERVAL, SETTINGS_SCAN_INTERVAL as SETTINGS_SCAN_INTERVAL, SUBSYSTEM_BATTERIES as SUBSYSTEM_BATTERIES, SUBSYSTEM_COMMON as SUBSYSTEM_COMMON, SUBSYSTEM_EXPORT_CONTROL as SUBSYSTEM_EXPORT_CONTROL, SUBSYSTEM_GRID_STATUS as SUBSYSTEM_GRID_STATUS, SUBSYSTEM_INVERTER as SUBSYSTEM_INVERTER, SUBSYSTEM_METERS as SUBSYSTEM_METERS, SUBSYSTEM_POWER_CONTROL as SUBSYSTEM_POWER_CONTROL, SUBSYSTEM_STORAGE_CONTROL as SUBSYSTEM_STORAGE_CONTROL
from .coordinator import SolarEdgeModbusConfigEntry as SolarEdgeModbusConfigEntry, SolarEdgeModbusDataUpdateCoordinator as SolarEdgeModbusDataUpdateCoordinator, SolarEdgeModbusRuntimeData as SolarEdgeModbusRuntimeData
from .entity import attachment_identity as attachment_identity, inverter_device_info as inverter_device_info
from .helpers import create_modbus_params as create_modbus_params
from _typeshed import Incomplete
from collections.abc import Set as AbstractSet
from datetime import datetime
from homeassistant.components.modbus import async_get_unit as async_get_unit
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryError as ConfigEntryError, ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from modbus_connection import ModbusUnit as ModbusUnit
from solaredged import SolarEdge

PLATFORMS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry) -> bool: ...
def _attachment_identities(solaredge: SolarEdge) -> frozenset[str]: ...
def _probed_blocks(solaredge: SolarEdge) -> dict[str, int]: ...
async def _async_reload_when_attachments_change(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, unit: ModbusUnit, _now: datetime) -> None: ...
def _async_remove_stale_devices(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry, solaredge: SolarEdge, serial_number: str, *, silent: AbstractSet[str]) -> None: ...
async def async_unload_entry(hass: HomeAssistant, entry: SolarEdgeModbusConfigEntry) -> bool: ...
