from .const import DOMAIN as DOMAIN
from .data import UFPConfigEntry as UFPConfigEntry
from _typeshed import Incomplete
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity
from typing import TypedDict
from uiprotect import ProtectApiClient as ProtectApiClient
from uiprotect.data import Bootstrap as Bootstrap

_LOGGER: Incomplete

class EntityRef(TypedDict):
    id: str
    platform: Platform

class EntityUsage(TypedDict):
    automations: dict[str, list[str]]
    scripts: dict[str, list[str]]

@callback
def check_if_used(hass: HomeAssistant, entry: UFPConfigEntry, entities: dict[str, EntityRef]) -> dict[str, EntityUsage]: ...
@callback
def create_repair_if_used(hass: HomeAssistant, entry: UFPConfigEntry, breaks_in: str, entities: dict[str, EntityRef]) -> None: ...
async def async_migrate_data(hass: HomeAssistant, entry: UFPConfigEntry, protect: ProtectApiClient, bootstrap: Bootstrap) -> None: ...
@callback
def async_migrate_insecure_cameras(hass: HomeAssistant, entry: UFPConfigEntry) -> None: ...
@callback
def _async_repair_if_used(hass: HomeAssistant, entity: er.RegistryEntry, issue_id: str, translation_key: str, placeholders: dict[str, str] | None = None) -> None: ...
@callback
def async_remove_package_binary_sensor(hass: HomeAssistant, entry: UFPConfigEntry) -> None: ...
@callback
def async_deprecate_hdr(hass: HomeAssistant, entry: UFPConfigEntry) -> None: ...
