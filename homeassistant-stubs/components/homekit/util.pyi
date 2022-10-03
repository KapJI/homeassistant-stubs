import socket
from .const import AUDIO_CODEC_COPY as AUDIO_CODEC_COPY, AUDIO_CODEC_OPUS as AUDIO_CODEC_OPUS, CONF_AUDIO_CODEC as CONF_AUDIO_CODEC, CONF_AUDIO_MAP as CONF_AUDIO_MAP, CONF_AUDIO_PACKET_SIZE as CONF_AUDIO_PACKET_SIZE, CONF_FEATURE as CONF_FEATURE, CONF_FEATURE_LIST as CONF_FEATURE_LIST, CONF_LINKED_BATTERY_CHARGING_SENSOR as CONF_LINKED_BATTERY_CHARGING_SENSOR, CONF_LINKED_BATTERY_SENSOR as CONF_LINKED_BATTERY_SENSOR, CONF_LINKED_DOORBELL_SENSOR as CONF_LINKED_DOORBELL_SENSOR, CONF_LINKED_HUMIDITY_SENSOR as CONF_LINKED_HUMIDITY_SENSOR, CONF_LINKED_MOTION_SENSOR as CONF_LINKED_MOTION_SENSOR, CONF_LINKED_OBSTRUCTION_SENSOR as CONF_LINKED_OBSTRUCTION_SENSOR, CONF_LOW_BATTERY_THRESHOLD as CONF_LOW_BATTERY_THRESHOLD, CONF_MAX_FPS as CONF_MAX_FPS, CONF_MAX_HEIGHT as CONF_MAX_HEIGHT, CONF_MAX_WIDTH as CONF_MAX_WIDTH, CONF_STREAM_ADDRESS as CONF_STREAM_ADDRESS, CONF_STREAM_COUNT as CONF_STREAM_COUNT, CONF_STREAM_SOURCE as CONF_STREAM_SOURCE, CONF_SUPPORT_AUDIO as CONF_SUPPORT_AUDIO, CONF_VIDEO_CODEC as CONF_VIDEO_CODEC, CONF_VIDEO_MAP as CONF_VIDEO_MAP, CONF_VIDEO_PACKET_SIZE as CONF_VIDEO_PACKET_SIZE, DEFAULT_AUDIO_CODEC as DEFAULT_AUDIO_CODEC, DEFAULT_AUDIO_MAP as DEFAULT_AUDIO_MAP, DEFAULT_AUDIO_PACKET_SIZE as DEFAULT_AUDIO_PACKET_SIZE, DEFAULT_LOW_BATTERY_THRESHOLD as DEFAULT_LOW_BATTERY_THRESHOLD, DEFAULT_MAX_FPS as DEFAULT_MAX_FPS, DEFAULT_MAX_HEIGHT as DEFAULT_MAX_HEIGHT, DEFAULT_MAX_WIDTH as DEFAULT_MAX_WIDTH, DEFAULT_STREAM_COUNT as DEFAULT_STREAM_COUNT, DEFAULT_SUPPORT_AUDIO as DEFAULT_SUPPORT_AUDIO, DEFAULT_VIDEO_CODEC as DEFAULT_VIDEO_CODEC, DEFAULT_VIDEO_MAP as DEFAULT_VIDEO_MAP, DEFAULT_VIDEO_PACKET_SIZE as DEFAULT_VIDEO_PACKET_SIZE, DOMAIN as DOMAIN, FEATURE_ON_OFF as FEATURE_ON_OFF, FEATURE_PLAY_PAUSE as FEATURE_PLAY_PAUSE, FEATURE_PLAY_STOP as FEATURE_PLAY_STOP, FEATURE_TOGGLE_MUTE as FEATURE_TOGGLE_MUTE, HOMEKIT_PAIRING_QR as HOMEKIT_PAIRING_QR, HOMEKIT_PAIRING_QR_SECRET as HOMEKIT_PAIRING_QR_SECRET, MAX_NAME_LENGTH as MAX_NAME_LENGTH, TYPE_FAUCET as TYPE_FAUCET, TYPE_OUTLET as TYPE_OUTLET, TYPE_SHOWER as TYPE_SHOWER, TYPE_SPRINKLER as TYPE_SPRINKLER, TYPE_SWITCH as TYPE_SWITCH, TYPE_VALVE as TYPE_VALVE, VIDEO_CODEC_COPY as VIDEO_CODEC_COPY, VIDEO_CODEC_H264_OMX as VIDEO_CODEC_H264_OMX, VIDEO_CODEC_LIBX264 as VIDEO_CODEC_LIBX264
from _typeshed import Incomplete
from homeassistant.components import binary_sensor as binary_sensor, media_player as media_player, persistent_notification as persistent_notification, sensor as sensor
from homeassistant.components.media_player import MediaPlayerDeviceClass as MediaPlayerDeviceClass, MediaPlayerEntityFeature as MediaPlayerEntityFeature
from homeassistant.components.remote import RemoteEntityFeature as RemoteEntityFeature
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_DEVICE_CLASS as ATTR_DEVICE_CLASS, ATTR_SUPPORTED_FEATURES as ATTR_SUPPORTED_FEATURES, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT, CONF_TYPE as CONF_TYPE, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.storage import STORAGE_DIR as STORAGE_DIR
from homeassistant.util.unit_conversion import TemperatureConverter as TemperatureConverter
from pyhap.accessory import Accessory as Accessory
from typing import Any

_LOGGER: Incomplete
NUMBERS_ONLY_RE: Incomplete
VERSION_RE: Incomplete
MAX_VERSION_PART: Incomplete
MAX_PORT: int
VALID_VIDEO_CODECS: Incomplete
VALID_AUDIO_CODECS: Incomplete
BASIC_INFO_SCHEMA: Incomplete
FEATURE_SCHEMA: Incomplete
CAMERA_SCHEMA: Incomplete
HUMIDIFIER_SCHEMA: Incomplete
COVER_SCHEMA: Incomplete
CODE_SCHEMA: Incomplete
MEDIA_PLAYER_SCHEMA: Incomplete
SWITCH_TYPE_SCHEMA: Incomplete
HOMEKIT_CHAR_TRANSLATIONS: Incomplete

def validate_entity_config(values: dict) -> dict[str, dict]: ...
def get_media_player_features(state: State) -> list[str]: ...
def validate_media_player_features(state: State, feature_list: str) -> bool: ...
def async_show_setup_message(hass: HomeAssistant, entry_id: str, bridge_name: str, pincode: bytes, uri: str) -> None: ...
def async_dismiss_setup_message(hass: HomeAssistant, entry_id: str) -> None: ...
def convert_to_float(state: Any) -> Union[float, None]: ...
def coerce_int(state: str) -> int: ...
def cleanup_name_for_homekit(name: Union[str, None]) -> str: ...
def temperature_to_homekit(temperature: Union[float, int], unit: str) -> float: ...
def temperature_to_states(temperature: Union[float, int], unit: str) -> float: ...
def density_to_air_quality(density: float) -> int: ...
def density_to_air_quality_pm10(density: float) -> int: ...
def get_persist_filename_for_entry_id(entry_id: str) -> str: ...
def get_aid_storage_filename_for_entry_id(entry_id: str) -> str: ...
def get_persist_fullpath_for_entry_id(hass: HomeAssistant, entry_id: str) -> str: ...
def get_aid_storage_fullpath_for_entry_id(hass: HomeAssistant, entry_id: str) -> str: ...
def _format_version_part(version_part: str) -> str: ...
def format_version(version: str) -> Union[str, None]: ...
def _is_zero_but_true(value: Any) -> bool: ...
def remove_state_files_for_entry_id(hass: HomeAssistant, entry_id: str) -> bool: ...
def _get_test_socket() -> socket.socket: ...
def async_port_is_available(port: int) -> bool: ...
def async_find_next_available_port(hass: HomeAssistant, start_port: int) -> int: ...
def _async_find_next_available_port(start_port: int, exclude_ports: set) -> int: ...
def pid_is_alive(pid: int) -> bool: ...
def accessory_friendly_name(hass_name: str, accessory: Accessory) -> str: ...
def state_needs_accessory_mode(state: State) -> bool: ...
def state_changed_event_is_same_state(event: Event) -> bool: ...
