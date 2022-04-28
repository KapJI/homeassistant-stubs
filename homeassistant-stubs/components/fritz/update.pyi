from .common import AvmWrapper as AvmWrapper, FritzBoxBaseEntity as FritzBoxBaseEntity
from .const import DOMAIN as DOMAIN
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxUpdateEntity(FritzBoxBaseEntity, UpdateEntity):
    _attr_supported_features: Any
    _attr_title: str
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str) -> None: ...
    @property
    def installed_version(self) -> Union[str, None]: ...
    @property
    def latest_version(self) -> Union[str, None]: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
