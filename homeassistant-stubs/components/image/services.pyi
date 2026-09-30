from . import ImageEntity as ImageEntity
from .const import ATTR_FILENAME as ATTR_FILENAME, DATA_COMPONENT as DATA_COMPONENT, IMAGE_TIMEOUT as IMAGE_TIMEOUT, SERVICE_SNAPSHOT as SERVICE_SNAPSHOT
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.typing import VolDictType as VolDictType

IMAGE_SERVICE_SNAPSHOT: VolDictType

async def _async_handle_snapshot_service(image: ImageEntity, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
