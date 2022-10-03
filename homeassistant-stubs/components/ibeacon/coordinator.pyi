import time
from .const import CONF_IGNORE_ADDRESSES as CONF_IGNORE_ADDRESSES, DOMAIN as DOMAIN, MAX_IDS as MAX_IDS, SIGNAL_IBEACON_DEVICE_NEW as SIGNAL_IBEACON_DEVICE_NEW, SIGNAL_IBEACON_DEVICE_SEEN as SIGNAL_IBEACON_DEVICE_SEEN, SIGNAL_IBEACON_DEVICE_UNAVAILABLE as SIGNAL_IBEACON_DEVICE_UNAVAILABLE, UNAVAILABLE_TIMEOUT as UNAVAILABLE_TIMEOUT, UPDATE_INTERVAL as UPDATE_INTERVAL
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components import bluetooth as bluetooth
from homeassistant.components.bluetooth.match import BluetoothCallbackMatcher as BluetoothCallbackMatcher
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceRegistry as DeviceRegistry
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.event import async_track_time_interval as async_track_time_interval
from ibeacon_ble import iBeaconAdvertisement as iBeaconAdvertisement

MONOTONIC_TIME = time.monotonic

def signal_unavailable(unique_id: str) -> str: ...
def signal_seen(unique_id: str) -> str: ...
def make_short_address(address: str) -> str: ...
def async_name(service_info: bluetooth.BluetoothServiceInfoBleak, ibeacon_advertisement: iBeaconAdvertisement, unique_address: bool = ...) -> str: ...
def _async_dispatch_update(hass: HomeAssistant, device_id: str, service_info: bluetooth.BluetoothServiceInfoBleak, ibeacon_advertisement: iBeaconAdvertisement, new: bool, unique_address: bool) -> None: ...

class IBeaconCoordinator:
    hass: Incomplete
    _entry: Incomplete
    _dev_reg: Incomplete
    _ignore_addresses: Incomplete
    _last_ibeacon_advertisement_by_unique_id: Incomplete
    _group_ids_by_address: Incomplete
    _unique_ids_by_address: Incomplete
    _unique_ids_by_group_id: Incomplete
    _addresses_by_group_id: Incomplete
    _unavailable_trackers: Incomplete
    _group_ids_random_macs: Incomplete
    _last_seen_by_group_id: Incomplete
    _unavailable_group_ids: Incomplete
    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, registry: DeviceRegistry) -> None: ...
    def _async_handle_unavailable(self, service_info: bluetooth.BluetoothServiceInfoBleak) -> None: ...
    def _async_cancel_unavailable_tracker(self, address: str) -> None: ...
    def _async_ignore_address(self, address: str) -> None: ...
    def _async_purge_untrackable_entities(self, unique_ids: set[str]) -> None: ...
    def _async_convert_random_mac_tracking(self, group_id: str, service_info: bluetooth.BluetoothServiceInfoBleak, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    def _async_track_ibeacon_with_unique_address(self, address: str, group_id: str, unique_id: str) -> None: ...
    def _async_update_ibeacon(self, service_info: bluetooth.BluetoothServiceInfoBleak, change: bluetooth.BluetoothChange) -> None: ...
    def _async_update_ibeacon_with_random_mac(self, group_id: str, service_info: bluetooth.BluetoothServiceInfoBleak, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    def _async_update_ibeacon_with_unique_address(self, group_id: str, service_info: bluetooth.BluetoothServiceInfoBleak, ibeacon_advertisement: iBeaconAdvertisement) -> None: ...
    def _async_stop(self) -> None: ...
    def _async_check_unavailable_groups_with_random_macs(self) -> None: ...
    def _async_update_rssi(self) -> None: ...
    def _async_update(self, _now: datetime) -> None: ...
    def _async_restore_from_registry(self) -> None: ...
    def async_start(self) -> None: ...
