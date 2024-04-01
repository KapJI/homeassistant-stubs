from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.automation import automations_with_entity as automations_with_entity
from homeassistant.components.script import scripts_with_entity as scripts_with_entity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity
from pyunifiprotect import ProtectApiClient as ProtectApiClient
from pyunifiprotect.data import Bootstrap as Bootstrap
from typing_extensions import TypedDict

_LOGGER: Incomplete

class EntityRef(TypedDict):
    id: str
    platform: Platform

class EntityUsage(TypedDict):
    automations: dict[str, list[str]]
    scripts: dict[str, list[str]]

def check_if_used(hass: HomeAssistant, entry: ConfigEntry, entities: dict[str, EntityRef]) -> dict[str, EntityUsage]: ...
def create_repair_if_used(hass: HomeAssistant, entry: ConfigEntry, breaks_in: str, entities: dict[str, EntityRef]) -> None: ...
async def async_migrate_data(hass: HomeAssistant, entry: ConfigEntry, protect: ProtectApiClient, bootstrap: Bootstrap) -> None: ...
def async_deprecate_hdr_package(hass: HomeAssistant, entry: ConfigEntry) -> None: ...
