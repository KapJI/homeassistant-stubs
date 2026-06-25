from . import IBeaconConfigEntry as IBeaconConfigEntry
from .const import SIGNAL_IBEACON_DEVICE_NEW as SIGNAL_IBEACON_DEVICE_NEW
from .coordinator import IBeaconCoordinator as IBeaconCoordinator
from .entity import IBeaconEntity as IBeaconEntity
from _typeshed import Incomplete
from homeassistant.components.device_tracker import BaseScannerEntity as BaseScannerEntity, SourceType as SourceType
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ibeacon_ble import iBeaconAdvertisement as iBeaconAdvertisement
from typing import override

async def async_setup_entry(hass: HomeAssistant, entry: IBeaconConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class IBeaconTrackerEntity(IBeaconEntity, BaseScannerEntity):
    _attr_name: Incomplete
    _attr_source_type: SourceType
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _active: bool
    def __init__(self, coordinator: IBeaconCoordinator, identifier: str, device_unique_id: str, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @property
    @override
    def is_connected(self) -> bool: ...
    _ibeacon_advertisement: Incomplete
    @callback
    @override
    def _async_seen(self, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    @callback
    @override
    def _async_unavailable(self) -> None: ...
