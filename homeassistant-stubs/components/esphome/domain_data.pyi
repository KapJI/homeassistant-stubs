from .bluetooth.cache import ESPHomeBluetoothCache as ESPHomeBluetoothCache
from .const import DOMAIN as DOMAIN
from .entry_data import ESPHomeStorage as ESPHomeStorage, RuntimeEntryData as RuntimeEntryData
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import Self

STORAGE_VERSION: int

class DomainData:
    _entry_datas: dict[str, RuntimeEntryData]
    _stores: dict[str, ESPHomeStorage]
    bluetooth_cache: ESPHomeBluetoothCache
    def get_entry_data(self, entry: ConfigEntry) -> RuntimeEntryData: ...
    def set_entry_data(self, entry: ConfigEntry, entry_data: RuntimeEntryData) -> None: ...
    def pop_entry_data(self, entry: ConfigEntry) -> RuntimeEntryData: ...
    def get_or_create_store(self, hass: HomeAssistant, entry: ConfigEntry) -> ESPHomeStorage: ...
    @classmethod
    def get(cls, hass: HomeAssistant) -> Self: ...
    def __init__(self, _entry_datas, _stores, bluetooth_cache) -> None: ...
