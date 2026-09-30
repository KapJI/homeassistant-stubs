from . import Camera as Camera
from .const import ATTR_FILENAME as ATTR_FILENAME, ATTR_FORMAT as ATTR_FORMAT, ATTR_MEDIA_PLAYER as ATTR_MEDIA_PLAYER, CAMERA_IMAGE_TIMEOUT as CAMERA_IMAGE_TIMEOUT, CONF_DURATION as CONF_DURATION, CONF_LOOKBACK as CONF_LOOKBACK, DATA_COMPONENT as DATA_COMPONENT, SERVICE_DISABLE_MOTION as SERVICE_DISABLE_MOTION, SERVICE_ENABLE_MOTION as SERVICE_ENABLE_MOTION, SERVICE_PLAY_STREAM as SERVICE_PLAY_STREAM, SERVICE_RECORD as SERVICE_RECORD, SERVICE_SNAPSHOT as SERVICE_SNAPSHOT
from .helper import async_get_stream_image as async_get_stream_image, async_stream_endpoint_url as async_stream_endpoint_url
from homeassistant.components.media_player import ATTR_MEDIA_CONTENT_ID as ATTR_MEDIA_CONTENT_ID, ATTR_MEDIA_CONTENT_TYPE as ATTR_MEDIA_CONTENT_TYPE, SERVICE_PLAY_MEDIA as SERVICE_PLAY_MEDIA
from homeassistant.components.stream import FORMAT_CONTENT_TYPE as FORMAT_CONTENT_TYPE, OUTPUT_FORMATS as OUTPUT_FORMATS
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_FILENAME as CONF_FILENAME, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.network import get_url as get_url
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import VolDictType as VolDictType

CAMERA_SERVICE_SNAPSHOT: VolDictType
CAMERA_SERVICE_PLAY_STREAM: VolDictType
CAMERA_SERVICE_RECORD: VolDictType

async def _async_handle_snapshot_service(camera: Camera, service_call: ServiceCall) -> None: ...
async def _async_handle_play_stream_service(camera: Camera, service_call: ServiceCall) -> None: ...
async def _async_handle_record_service(camera: Camera, service_call: ServiceCall) -> None: ...
@callback
def async_setup_services(hass: HomeAssistant) -> None: ...
