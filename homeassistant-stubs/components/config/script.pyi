from .const import ACTION_DELETE as ACTION_DELETE
from .view import EditKeyBasedConfigView as EditKeyBasedConfigView
from homeassistant.components.script import DOMAIN as DOMAIN
from homeassistant.components.script.config import SCRIPT_ENTITY_SCHEMA as SCRIPT_ENTITY_SCHEMA, async_validate_config_item as async_validate_config_item
from homeassistant.config import SCRIPT_CONFIG_PATH as SCRIPT_CONFIG_PATH
from homeassistant.const import SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from typing import Any

def async_setup(hass: HomeAssistant) -> bool: ...

class EditScriptConfigView(EditKeyBasedConfigView):
    def _write_value(self, hass: HomeAssistant, data: dict[str, dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
