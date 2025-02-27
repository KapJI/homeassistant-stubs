from .const import DOMAIN as DOMAIN
from .coordinator import CertExpiryConfigEntry as CertExpiryConfigEntry, CertExpiryDataUpdateCoordinator as CertExpiryDataUpdateCoordinator
from .entity import CertExpiryEntity as CertExpiryEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: CertExpiryConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SSLCertificateTimestamp(CertExpiryEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: CertExpiryDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> datetime | None: ...
