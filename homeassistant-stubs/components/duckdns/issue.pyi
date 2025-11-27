from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue

@callback
def deprecate_yaml_issue(hass: HomeAssistant, *, import_success: bool) -> None: ...
