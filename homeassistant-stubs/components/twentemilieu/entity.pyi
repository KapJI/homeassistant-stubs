from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from datetime import date
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity, DataUpdateCoordinator as DataUpdateCoordinator
from twentemilieu import WasteType

class TwenteMilieuEntity(CoordinatorEntity[DataUpdateCoordinator[dict[WasteType, list[date]]]], Entity):
    _attr_has_entity_name: bool
    _attr_device_info: Incomplete
    def __init__(self, coordinator: DataUpdateCoordinator[dict[WasteType, list[date]]], entry: ConfigEntry) -> None: ...
