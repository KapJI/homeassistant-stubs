from . import ACTION_DELETE as ACTION_DELETE, EditIdBasedConfigView as EditIdBasedConfigView
from homeassistant.components.scene import DOMAIN as DOMAIN, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.config import SCENE_CONFIG_PATH as SCENE_CONFIG_PATH
from homeassistant.const import CONF_ID as CONF_ID, SERVICE_RELOAD as SERVICE_RELOAD
from homeassistant.core import HomeAssistant as HomeAssistant
from typing import Any

async def async_setup(hass: HomeAssistant) -> bool: ...

class EditSceneConfigView(EditIdBasedConfigView):
    def _write_value(self, hass: HomeAssistant, data: list[dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
