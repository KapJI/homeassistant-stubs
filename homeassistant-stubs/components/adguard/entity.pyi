from .const import DATA_ADGUARD_VERSION as DATA_ADGUARD_VERSION, DOMAIN as DOMAIN, LOGGER as LOGGER
from _typeshed import Incomplete
from adguardhome import AdGuardHome as AdGuardHome
from homeassistant.config_entries import ConfigEntry as ConfigEntry, SOURCE_HASSIO as SOURCE_HASSIO
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity

class AdGuardHomeEntity(Entity):
    _attr_has_entity_name: bool
    _attr_available: bool
    _entry: Incomplete
    adguard: Incomplete
    def __init__(self, adguard: AdGuardHome, entry: ConfigEntry) -> None: ...
    async def async_update(self) -> None: ...
    async def _adguard_update(self) -> None: ...
    @property
    def device_info(self) -> DeviceInfo: ...
