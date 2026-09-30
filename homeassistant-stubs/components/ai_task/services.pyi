import probatio
from .const import ATTR_ATTACHMENTS as ATTR_ATTACHMENTS, ATTR_INSTRUCTIONS as ATTR_INSTRUCTIONS, ATTR_REQUIRED as ATTR_REQUIRED, ATTR_STRUCTURE as ATTR_STRUCTURE, ATTR_TASK_NAME as ATTR_TASK_NAME, DOMAIN as DOMAIN, SERVICE_GENERATE_DATA as SERVICE_GENERATE_DATA, SERVICE_GENERATE_IMAGE as SERVICE_GENERATE_IMAGE
from .task import async_generate_data as async_generate_data, async_generate_image as async_generate_image
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DESCRIPTION as CONF_DESCRIPTION, CONF_SELECTOR as CONF_SELECTOR
from homeassistant.core import HassJobType as HassJobType, HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, ServiceResponse as ServiceResponse, SupportsResponse as SupportsResponse, callback as callback
from homeassistant.helpers import selector as selector
from typing import Any

STRUCTURE_FIELD_SCHEMA: Incomplete

def _validate_structure_fields(value: dict[str, Any]) -> probatio.Schema: ...
async def async_service_generate_data(call: ServiceCall) -> ServiceResponse: ...
async def async_service_generate_image(call: ServiceCall) -> ServiceResponse: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
