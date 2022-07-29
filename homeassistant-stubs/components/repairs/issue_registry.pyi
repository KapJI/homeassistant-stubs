from .models import IssueSeverity as IssueSeverity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store

DATA_REGISTRY: str
EVENT_REPAIRS_ISSUE_REGISTRY_UPDATED: str
STORAGE_KEY: str
STORAGE_VERSION: int
SAVE_DELAY: int

class IssueEntry:
    active: bool
    breaks_in_ha_version: Union[str, None]
    created: datetime
    dismissed_version: Union[str, None]
    domain: str
    is_fixable: Union[bool, None]
    issue_id: str
    issue_domain: Union[str, None]
    learn_more_url: Union[str, None]
    severity: Union[IssueSeverity, None]
    translation_key: Union[str, None]
    translation_placeholders: Union[dict[str, str], None]
    def __init__(self, active, breaks_in_ha_version, created, dismissed_version, domain, is_fixable, issue_id, issue_domain, learn_more_url, severity, translation_key, translation_placeholders) -> None: ...

class IssueRegistry:
    hass: Incomplete
    issues: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    def async_get_issue(self, domain: str, issue_id: str) -> Union[IssueEntry, None]: ...
    def async_get_or_create(self, domain: str, issue_id: str, *, issue_domain: Union[str, None] = ..., breaks_in_ha_version: Union[str, None] = ..., is_fixable: bool, learn_more_url: Union[str, None] = ..., severity: IssueSeverity, translation_key: str, translation_placeholders: Union[dict[str, str], None] = ...) -> IssueEntry: ...
    def async_delete(self, domain: str, issue_id: str) -> None: ...
    def async_ignore(self, domain: str, issue_id: str, ignore: bool) -> IssueEntry: ...
    async def async_load(self) -> None: ...
    def async_schedule_save(self) -> None: ...
    def _data_to_save(self) -> dict[str, list[dict[str, Union[str, None]]]]: ...

def async_get(hass: HomeAssistant) -> IssueRegistry: ...
async def async_load(hass: HomeAssistant) -> None: ...
