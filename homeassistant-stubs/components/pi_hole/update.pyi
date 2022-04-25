from . import PiHoleEntity as PiHoleEntity
from .const import DATA_KEY_API as DATA_KEY_API, DATA_KEY_COORDINATOR as DATA_KEY_COORDINATOR, DOMAIN as DOMAIN
from collections.abc import Callable as Callable
from hole import Hole as Hole
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any

class PiHoleUpdateEntityDescription(UpdateEntityDescription):
    installed_version: Callable[[dict], Union[str, None]]
    latest_version: Callable[[dict], Union[str, None]]
    release_base_url: Union[str, None]
    title: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, installed_version, latest_version, release_base_url, title) -> None: ...

UPDATE_ENTITY_TYPES: tuple[PiHoleUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class PiHoleUpdateEntity(PiHoleEntity, UpdateEntity):
    entity_description: PiHoleUpdateEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    _attr_title: Any
    def __init__(self, api: Hole, coordinator: DataUpdateCoordinator, name: str, server_unique_id: str, description: PiHoleUpdateEntityDescription) -> None: ...
    @property
    def installed_version(self) -> Union[str, None]: ...
    @property
    def latest_version(self) -> Union[str, None]: ...
    @property
    def release_url(self) -> Union[str, None]: ...