from .const import DOMAIN as DOMAIN, INFO_SKILLS_MAPPING as INFO_SKILLS_MAPPING
from .coordinator import AmazonConfigEntry as AmazonConfigEntry
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState
from homeassistant.const import ATTR_DEVICE_ID as ATTR_DEVICE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import device_registry as dr

ATTR_TEXT_COMMAND: str
ATTR_SOUND: str
ATTR_INFO_SKILL: str
SCHEMA_SOUND_SERVICE: Incomplete
SCHEMA_CUSTOM_COMMAND: Incomplete
SCHEMA_INFO_SKILL: Incomplete

@callback
def async_get_entry_id_for_service_call(call: ServiceCall) -> tuple[dr.DeviceEntry, AmazonConfigEntry]: ...
async def _async_execute_action(call: ServiceCall, attribute: str) -> None: ...
async def async_send_sound_notification(call: ServiceCall) -> None: ...
async def async_send_text_command(call: ServiceCall) -> None: ...
async def async_send_info_skill(call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
