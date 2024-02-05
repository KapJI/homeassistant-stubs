from . import ACTION_DELETE as ACTION_DELETE, EditIdBasedConfigView as EditIdBasedConfigView
from homeassistant.components.automation.config import DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA, async_validate_config_item as async_validate_config_item
from homeassistant.config import AUTOMATION_CONFIG_PATH as AUTOMATION_CONFIG_PATH
from homeassistant.const import CONF_ID as CONF_ID, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_setup(hass: HomeAssistant) -> bool: ...

class EditAutomationConfigView(EditIdBasedConfigView):
    def _write_value(self, hass: HomeAssistant, data: list[dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
