from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.json import JSONEncoder as JSONEncoder
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import TypedDict

_LOGGER: Incomplete
ENCRYPTION_KEY_STORAGE_VERSION: int
ENCRYPTION_KEY_STORAGE_KEY: str

class EncryptionKeyData(TypedDict):
    keys: dict[str, str]

KEY_ENCRYPTION_STORAGE: HassKey[ESPHomeEncryptionKeyStorage]

class ESPHomeEncryptionKeyStorage:
    hass: Incomplete
    _store: Incomplete
    _data: EncryptionKeyData | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_load(self) -> None: ...
    async def async_save(self) -> None: ...
    async def async_get_key(self, mac_address: str) -> str | None: ...
    async def async_store_key(self, mac_address: str, key: str) -> None: ...
    async def async_remove_key(self, mac_address: str) -> None: ...

async def async_get_encryption_key_storage(hass: HomeAssistant) -> ESPHomeEncryptionKeyStorage: ...
