from . import SynoApi as SynoApi
from .const import COORDINATOR_CENTRAL as COORDINATOR_CENTRAL, DOMAIN as DOMAIN, SYNO_API as SYNO_API
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from _typeshed import Incomplete
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

class SynologyDSMUpdateEntityEntityDescription(UpdateEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement) -> None: ...

UPDATE_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMUpdateEntity(SynologyDSMBaseEntity, UpdateEntity):
    entity_description: SynologyDSMUpdateEntityEntityDescription
    _attr_title: str
    @property
    def installed_version(self) -> Union[str, None]: ...
    @property
    def latest_version(self) -> Union[str, None]: ...
    @property
    def release_url(self) -> Union[str, None]: ...
