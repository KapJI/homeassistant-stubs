from .const import CONF_SERVER as CONF_SERVER, DOMAIN as DOMAIN
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_SENDER as CONF_SENDER
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue, create_issue as create_issue
from typing import Any

@callback
def async_deprecate_yaml_issue(hass: HomeAssistant, config: dict[str, Any], *, import_success: bool = True) -> None: ...
def deprecated_notify_action_call(hass: HomeAssistant, service_name: str) -> None: ...
