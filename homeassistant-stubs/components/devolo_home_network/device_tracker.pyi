from .const import CONNECTED_STATIONS as CONNECTED_STATIONS, CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, MAC_ADDRESS as MAC_ADDRESS, WIFI_APTYPE as WIFI_APTYPE, WIFI_BANDS as WIFI_BANDS
from _typeshed import Incomplete
from devolo_plc_api.device import Device as Device
from homeassistant.components.device_tracker import SOURCE_TYPE_ROUTER as SOURCE_TYPE_ROUTER
from homeassistant.components.device_tracker.config_entry import ScannerEntity as ScannerEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import FREQUENCY_GIGAHERTZ as FREQUENCY_GIGAHERTZ, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as entity_registry
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DevoloScannerEntity(CoordinatorEntity, ScannerEntity):
    _device: Incomplete
    _mac: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator, device: Device, mac: str) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    @property
    def icon(self) -> str: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def mac_address(self) -> str: ...
    @property
    def source_type(self) -> str: ...
    @property
    def unique_id(self) -> str: ...
