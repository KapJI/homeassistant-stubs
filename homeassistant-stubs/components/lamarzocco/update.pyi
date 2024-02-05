from .const import DOMAIN as DOMAIN
from .entity import LaMarzoccoEntity as LaMarzoccoEntity, LaMarzoccoEntityDescription as LaMarzoccoEntityDescription
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from lmcloud import LMCloud as LaMarzoccoClient
from lmcloud.const import LaMarzoccoUpdateableComponent
from typing import Any

@dataclass(frozen=True, kw_only=True)
class LaMarzoccoUpdateEntityDescription(LaMarzoccoEntityDescription, UpdateEntityDescription):
    current_fw_fn: Callable[[LaMarzoccoClient], str]
    latest_fw_fn: Callable[[LaMarzoccoClient], str]
    component: LaMarzoccoUpdateableComponent
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, available_fn, supported_fn, current_fw_fn, latest_fw_fn, component) -> None: ...

ENTITIES: tuple[LaMarzoccoUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LaMarzoccoUpdateEntity(LaMarzoccoEntity, UpdateEntity):
    entity_description: LaMarzoccoUpdateEntityDescription
    _attr_supported_features: Incomplete
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str: ...
    _attr_in_progress: bool
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
