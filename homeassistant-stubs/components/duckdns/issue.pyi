from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue

def action_called_without_config_entry(hass: HomeAssistant) -> None: ...
