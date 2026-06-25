from .const import AI_ART_FRAME_UPLOAD_IMAGE_SERVICE as AI_ART_FRAME_UPLOAD_IMAGE_SERVICE, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

_LOGGER: Incomplete
UPLOAD_IMAGE_SCHEMA: Incomplete

async def handle_upload_image(call: ServiceCall) -> None: ...
def async_register_services(hass: HomeAssistant) -> None: ...
