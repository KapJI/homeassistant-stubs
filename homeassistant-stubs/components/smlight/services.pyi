from .const import DOMAIN as DOMAIN
from .coordinator import SmConfigEntry as SmConfigEntry
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.service import async_extract_config_entry_ids as async_extract_config_entry_ids

SERVICE_PLAY_RTTTL: str
ATTR_BPM: str
ATTR_DURATION: str
ATTR_OCTAVE: str
ATTR_NOTES: str
RTTTL_VALID_BPMS: list[int]

@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
