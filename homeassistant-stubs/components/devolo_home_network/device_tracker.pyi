from .const import CONNECTED_WIFI_CLIENTS as CONNECTED_WIFI_CLIENTS, DOMAIN as DOMAIN, WIFI_APTYPE as WIFI_APTYPE, WIFI_BANDS as WIFI_BANDS
from .coordinator import DevoloDataUpdateCoordinator as DevoloDataUpdateCoordinator, DevoloHomeNetworkConfigEntry as DevoloHomeNetworkConfigEntry
from _typeshed import Incomplete
from devolo_plc_api.device import Device as Device
from devolo_plc_api.device_api import ConnectedStationInfo
from homeassistant.components.device_tracker import ScannerEntity as ScannerEntity
from homeassistant.const import STATE_UNKNOWN as STATE_UNKNOWN, UnitOfFrequency as UnitOfFrequency
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: DevoloHomeNetworkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DevoloScannerEntity(CoordinatorEntity[DevoloDataUpdateCoordinator[dict[str, ConnectedStationInfo]]], ScannerEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _device: Incomplete
    _attr_mac_address: Incomplete
    _attr_name: Incomplete
    def __init__(self, coordinator: DevoloDataUpdateCoordinator[dict[str, ConnectedStationInfo]], device: Device, mac: str) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, str]: ...
    @property
    def is_connected(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
