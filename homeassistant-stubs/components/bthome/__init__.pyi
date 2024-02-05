from .const import BTHOME_BLE_EVENT as BTHOME_BLE_EVENT, BTHomeBleEvent as BTHomeBleEvent, CONF_BINDKEY as CONF_BINDKEY, CONF_DISCOVERED_EVENT_CLASSES as CONF_DISCOVERED_EVENT_CLASSES, CONF_SLEEPY_DEVICE as CONF_SLEEPY_DEVICE, DOMAIN as DOMAIN
from .coordinator import BTHomePassiveBluetoothProcessorCoordinator as BTHomePassiveBluetoothProcessorCoordinator
from _typeshed import Incomplete
from bthome_ble import BTHomeBluetoothDeviceData, SensorUpdate as SensorUpdate
from homeassistant.components.bluetooth import BluetoothScanningMode as BluetoothScanningMode, BluetoothServiceInfoBleak as BluetoothServiceInfoBleak
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import CONNECTION_BLUETOOTH as CONNECTION_BLUETOOTH, DeviceRegistry as DeviceRegistry, async_get as async_get
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send

PLATFORMS: list[Platform]
_LOGGER: Incomplete

def process_service_info(hass: HomeAssistant, entry: ConfigEntry, data: BTHomeBluetoothDeviceData, service_info: BluetoothServiceInfoBleak, device_registry: DeviceRegistry) -> SensorUpdate: ...
def format_event_dispatcher_name(address: str, event_class: str) -> str: ...
def format_discovered_event_class(address: str) -> str: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
