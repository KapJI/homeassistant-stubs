from .const import DOMAIN as DOMAIN, STATE_ATTR_TORRENT_INFO as STATE_ATTR_TORRENT_INFO, STATE_DOWNLOADING as STATE_DOWNLOADING, STATE_SEEDING as STATE_SEEDING, STATE_UP_DOWN as STATE_UP_DOWN, SUPPORTED_ORDER_MODES as SUPPORTED_ORDER_MODES
from .coordinator import TransmissionDataUpdateCoordinator as TransmissionDataUpdateCoordinator
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import STATE_IDLE as STATE_IDLE, UnitOfDataRate as UnitOfDataRate
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from transmission_rpc.torrent import Torrent as Torrent
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TransmissionSensor(CoordinatorEntity[TransmissionDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_translation_key: Incomplete
    _key: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: TransmissionDataUpdateCoordinator, sensor_translation_key: str, key: str) -> None: ...

class TransmissionSpeedSensor(TransmissionSensor):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_suggested_display_precision: int
    _attr_suggested_unit_of_measurement: Incomplete
    @property
    def native_value(self) -> float: ...

class TransmissionStatusSensor(TransmissionSensor):
    _attr_device_class: Incomplete
    _attr_options: Incomplete
    @property
    def native_value(self) -> str: ...

class TransmissionTorrentsSensor(TransmissionSensor):
    MODES: dict[str, list[str] | None]
    @property
    def native_unit_of_measurement(self) -> str: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @property
    def native_value(self) -> int: ...

def _filter_torrents(torrents: list[Torrent], statuses: list[str] | None = ...) -> list[Torrent]: ...
def _torrents_info(torrents: list[Torrent], order: str, limit: int, statuses: list[str] | None = ...) -> dict[str, Any]: ...
