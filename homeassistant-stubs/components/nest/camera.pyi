import datetime
from .const import DATA_DEVICE_MANAGER as DATA_DEVICE_MANAGER, DOMAIN as DOMAIN
from .device_info import NestDeviceInfo as NestDeviceInfo
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from google_nest_sdm.camera_traits import RtspStream as RtspStream
from google_nest_sdm.device import Device as Device
from google_nest_sdm.device_manager import DeviceManager as DeviceManager
from homeassistant.components.camera import Camera as Camera, CameraEntityFeature as CameraEntityFeature, StreamType as StreamType
from homeassistant.components.stream import CONF_EXTRA_PART_WAIT_TIME as CONF_EXTRA_PART_WAIT_TIME
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_point_in_utc_time as async_track_point_in_utc_time
from homeassistant.util.dt import utcnow as utcnow

_LOGGER: Incomplete
PLACEHOLDER: Incomplete
STREAM_EXPIRATION_BUFFER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class NestCamera(Camera):
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _device: Incomplete
    _attr_device_info: Incomplete
    _attr_brand: Incomplete
    _attr_model: Incomplete
    _stream: Incomplete
    _create_stream_url_lock: Incomplete
    _stream_refresh_unsub: Incomplete
    _attr_is_streaming: bool
    _attr_supported_features: Incomplete
    _rtsp_live_stream_trait: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: Device) -> None: ...
    @property
    def use_stream_for_stills(self) -> bool: ...
    @property
    def frontend_stream_type(self) -> StreamType | None: ...
    @property
    def available(self) -> bool: ...
    async def stream_source(self) -> str | None: ...
    def _schedule_stream_refresh(self) -> None: ...
    stream: Incomplete
    async def _handle_stream_refresh(self, now: datetime.datetime) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_camera_image(self, width: int | None = None, height: int | None = None) -> bytes | None: ...
    @classmethod
    def placeholder_image(cls) -> bytes: ...
    async def async_handle_web_rtc_offer(self, offer_sdp: str) -> str | None: ...
