from .common import AvmWrapper as AvmWrapper, FritzBoxBaseCoordinatorEntity as FritzBoxBaseCoordinatorEntity, FritzEntityDescription as FritzEntityDescription
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

class FritzUpdateEntityDescription(UpdateEntityDescription, FritzEntityDescription):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxUpdateEntity(FritzBoxBaseCoordinatorEntity, UpdateEntity):
    _attr_entity_category: Incomplete
    _attr_supported_features: Incomplete
    _attr_title: str
    entity_description: FritzUpdateEntityDescription
    def __init__(self, avm_wrapper: AvmWrapper, device_friendly_name: str) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def release_url(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
