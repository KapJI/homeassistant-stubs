from .storage import Store as Store
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.util.async_ import run_callback_threadsafe as run_callback_threadsafe
from typing import Any

DATA_REGISTRY: str
EVENT_REPAIRS_ISSUE_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION_MAJOR: int
STORAGE_VERSION_MINOR: int
SAVE_DELAY: int

class IssueSeverity(StrEnum):
    CRITICAL: str
    ERROR: str
    WARNING: str

class IssueEntry:
    active: bool
    breaks_in_ha_version: Union[str, None]
    created: datetime
    data: Union[dict[str, Union[str, int, float, None]], None]
    dismissed_version: Union[str, None]
    domain: str
    is_fixable: Union[bool, None]
    is_persistent: bool
    issue_domain: Union[str, None]
    issue_id: str
    learn_more_url: Union[str, None]
    severity: Union[IssueSeverity, None]
    translation_key: Union[str, None]
    translation_placeholders: Union[dict[str, str], None]
    def to_json(self) -> dict[str, Any]: ...
    def __init__(self, active, breaks_in_ha_version, created, data, dismissed_version, domain, is_fixable, is_persistent, issue_domain, issue_id, learn_more_url, severity, translation_key, translation_placeholders) -> None: ...

class IssueRegistryStore(Store[dict[str, list[dict[str, Any]]]]):
    async def _async_migrate_func(self, old_major_version: int, old_minor_version: int, old_data: dict[str, Any]) -> dict[str, Any]: ...

class IssueRegistry:
    hass: Incomplete
    issues: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_issue(self, domain: str, issue_id: str) -> Union[IssueEntry, None]: ...
    def async_get_or_create(self, domain: str, issue_id: str, *, breaks_in_ha_version: Union[str, None] = ..., data: Union[dict[str, Union[str, int, float, None]], None] = ..., is_fixable: bool, is_persistent: bool, issue_domain: Union[str, None] = ..., learn_more_url: Union[str, None] = ..., severity: IssueSeverity, translation_key: str, translation_placeholders: Union[dict[str, str], None] = ...) -> IssueEntry: ...
    def async_delete(self, domain: str, issue_id: str) -> None: ...
    def async_ignore(self, domain: str, issue_id: str, ignore: bool) -> IssueEntry: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Union[str, None]]]]: ...

def async_get(hass: HomeAssistant) -> IssueRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
def async_create_issue(hass: HomeAssistant, domain: str, issue_id: str, *, breaks_in_ha_version: Union[str, None] = ..., data: Union[dict[str, Union[str, int, float, None]], None] = ..., is_fixable: bool, is_persistent: bool = ..., issue_domain: Union[str, None] = ..., learn_more_url: Union[str, None] = ..., severity: IssueSeverity, translation_key: str, translation_placeholders: Union[dict[str, str], None] = ...) -> None: ...
def create_issue(hass: HomeAssistant, domain: str, issue_id: str, *, breaks_in_ha_version: Union[str, None] = ..., data: Union[dict[str, Union[str, int, float, None]], None] = ..., is_fixable: bool, is_persistent: bool = ..., issue_domain: Union[str, None] = ..., learn_more_url: Union[str, None] = ..., severity: IssueSeverity, translation_key: str, translation_placeholders: Union[dict[str, str], None] = ...) -> None: ...
def async_delete_issue(hass: HomeAssistant, domain: str, issue_id: str) -> None: ...
def delete_issue(hass: HomeAssistant, domain: str, issue_id: str) -> None: ...
def async_ignore_issue(hass: HomeAssistant, domain: str, issue_id: str, ignore: bool) -> None: ...
