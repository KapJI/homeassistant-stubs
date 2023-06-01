from . import ImapPollingDataUpdateCoordinator as ImapPollingDataUpdateCoordinator, ImapPushDataUpdateCoordinator as ImapPushDataUpdateCoordinator
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ImapSensor(CoordinatorEntity[ImapPushDataUpdateCoordinator | ImapPollingDataUpdateCoordinator], SensorEntity):
    _attr_icon: str
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: ImapPushDataUpdateCoordinator | ImapPollingDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> int | None: ...
