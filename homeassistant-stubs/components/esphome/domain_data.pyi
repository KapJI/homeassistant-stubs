from .const import DOMAIN as DOMAIN
from .entry_data import ESPHomeConfigEntry as ESPHomeConfigEntry, ESPHomeStorage as ESPHomeStorage, RuntimeEntryData as RuntimeEntryData
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from typing import Self

STORAGE_VERSION: int

@dataclass(slots=True)
class DomainData:
    _stores: dict[str, ESPHomeStorage] = ...
    def get_entry_data(self, entry: ESPHomeConfigEntry) -> RuntimeEntryData: ...
    def get_or_create_store(self, hass: HomeAssistant, entry: ESPHomeConfigEntry) -> ESPHomeStorage: ...
    @classmethod
    def get(cls, hass: HomeAssistant) -> Self: ...
    def __init__(self, _stores=...) -> None: ...
