from .const import CONF_MODBUS_PORT as CONF_MODBUS_PORT, DEFAULT_MODBUS_PORT as DEFAULT_MODBUS_PORT, DOMAIN as DOMAIN, FroniusDeviceInfo as FroniusDeviceInfo, SOLAR_NET_DISCOVERY_NEW as SOLAR_NET_DISCOVERY_NEW, SOLAR_NET_ID_SYSTEM as SOLAR_NET_ID_SYSTEM, SOLAR_NET_RESCAN_TIMER as SOLAR_NET_RESCAN_TIMER, SolarNetId as SolarNetId
from .coordinator import FroniusCoordinatorBase as FroniusCoordinatorBase, FroniusInverterUpdateCoordinator as FroniusInverterUpdateCoordinator, FroniusLoggerUpdateCoordinator as FroniusLoggerUpdateCoordinator, FroniusMeterUpdateCoordinator as FroniusMeterUpdateCoordinator, FroniusModbusInverterUpdateCoordinator as FroniusModbusInverterUpdateCoordinator, FroniusModbusSettingsUpdateCoordinator as FroniusModbusSettingsUpdateCoordinator, FroniusOhmpilotUpdateCoordinator as FroniusOhmpilotUpdateCoordinator, FroniusPowerFlowUpdateCoordinator as FroniusPowerFlowUpdateCoordinator, FroniusStorageUpdateCoordinator as FroniusStorageUpdateCoordinator
from _typeshed import Incomplete
from datetime import datetime
from fronius_modbus import FroniusModbusInverter
from homeassistant.components.modbus import async_get_unit as async_get_unit
from homeassistant.config_entries import ConfigEntry as ConfigEntry, ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_MODEL as ATTR_MODEL, ATTR_SW_VERSION as ATTR_SW_VERSION, CONF_HOST as CONF_HOST, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ConfigEntryNotReady as ConfigEntryNotReady, HomeAssistantError as HomeAssistantError
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from modbus_connection import ModbusTcpParams
from pyfronius import Fronius
from typing import Final

_LOGGER: Final[Incomplete]
PLATFORMS: Final[Incomplete]
type FroniusConfigEntry = ConfigEntry[FroniusSolarNet]

async def async_setup_entry(hass: HomeAssistant, entry: FroniusConfigEntry) -> bool: ...
async def async_migrate_entry(hass: HomeAssistant, entry: FroniusConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: FroniusConfigEntry) -> bool: ...
async def async_remove_config_entry_device(hass: HomeAssistant, config_entry: FroniusConfigEntry, device_entry: dr.AnyDeviceEntry) -> bool: ...

class FroniusSolarNet:
    hass: Incomplete
    config_entry: Incomplete
    coordinator_lock: Incomplete
    fronius: Incomplete
    host: str
    solar_net_device_id: Incomplete
    system_device_info: DeviceInfo | None
    inverter_coordinators: list[FroniusInverterUpdateCoordinator]
    logger_coordinator: FroniusLoggerUpdateCoordinator | None
    meter_coordinator: FroniusMeterUpdateCoordinator | None
    ohmpilot_coordinator: FroniusOhmpilotUpdateCoordinator | None
    power_flow_coordinator: FroniusPowerFlowUpdateCoordinator | None
    storage_coordinator: FroniusStorageUpdateCoordinator | None
    modbus_inverter_coordinators: list[FroniusModbusInverterUpdateCoordinator]
    modbus_settings_coordinators: list[FroniusModbusSettingsUpdateCoordinator]
    modbus_inverters: dict[SolarNetId, FroniusModbusInverter]
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, fronius: Fronius) -> None: ...
    async def init_devices(self) -> None: ...
    async def _create_solar_net_device(self) -> DeviceInfo: ...
    async def _init_devices_inverter(self, _now: datetime | None = None) -> None: ...
    async def _get_inverter_infos(self) -> list[FroniusDeviceInfo]: ...
    def _modbus_params(self) -> ModbusTcpParams | None: ...
    async def _init_modbus_inverter(self, inverter_info: FroniusDeviceInfo) -> None: ...
    async def _start_modbus_coordinator(self, coordinator: FroniusCoordinatorBase) -> bool: ...
    async def _modbus_control_allowed(self, modbus_inverter: FroniusModbusInverter, unit_id: int) -> bool: ...
    def _modbus_unit_id(self, solar_net_id: str) -> int | None: ...
    @staticmethod
    async def _init_optional_coordinator[_FroniusCoordinatorT: FroniusCoordinatorBase](coordinator: _FroniusCoordinatorT) -> _FroniusCoordinatorT | None: ...
