from .const import DOMAIN as DOMAIN
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback

@callback
def async_create_deprecation_issue_once(hass: HomeAssistant, issue_id: str, breaks_in_ha_version: str, translation_key: str | None = None, translation_placeholders: dict[str, str] | None = None) -> None: ...
