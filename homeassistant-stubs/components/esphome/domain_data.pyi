from .const import ESPHOME_DATA as ESPHOME_DATA
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, ESPHomeStorage as ESPHomeStorage, RuntimeEntryData as RuntimeEntryData
from dataclasses import dataclass, field
from functools import cache
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder

STORAGE_VERSION: int

@dataclass(slots=True)
class DomainData:
    _stores: dict[str, ESPHomeStorage] = field(default_factory=dict)
    def get_entry_data(self, entry: ESPHomeConfigEntry) -> RuntimeEntryData: ...
    def get_or_create_store(self, hass: HomeAssistant, entry: ESPHomeConfigEntry) -> ESPHomeStorage: ...
    @staticmethod
    @cache
    def get(hass: HomeAssistant) -> DomainData: ...
