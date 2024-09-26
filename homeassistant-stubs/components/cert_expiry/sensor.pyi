from . import CertExpiryConfigEntry as CertExpiryConfigEntry
from .const import DEFAULT_PORT as DEFAULT_PORT, DOMAIN as DOMAIN
from .coordinator import CertExpiryDataUpdateCoordinator as CertExpiryDataUpdateCoordinator
from .entity import CertExpiryEntity as CertExpiryEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_call_later as async_call_later
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType

SCAN_INTERVAL: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: CertExpiryConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SSLCertificateTimestamp(CertExpiryEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CertExpiryDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> datetime | None: ...
