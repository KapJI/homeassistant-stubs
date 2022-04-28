from . import SynoApi as SynoApi
from .const import CONF_SNAPSHOT_QUALITY as CONF_SNAPSHOT_QUALITY, COORDINATOR_CAMERAS as COORDINATOR_CAMERAS, DEFAULT_SNAPSHOT_QUALITY as DEFAULT_SNAPSHOT_QUALITY, DOMAIN as DOMAIN, SYNO_API as SYNO_API
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription, CameraEntityFeature as CameraEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from synology_dsm.api.surveillance_station import SynoCamera as SynoCamera
from typing import Any

_LOGGER: Any

class SynologyDSMCameraEntityDescription(CameraEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMCamera(SynologyDSMBaseEntity, Camera):
    _attr_supported_features: Any
    coordinator: DataUpdateCoordinator[dict[str, dict[str, SynoCamera]]]
    entity_description: SynologyDSMCameraEntityDescription
    snapshot_quality: Any
    def __init__(self, api: SynoApi, coordinator: DataUpdateCoordinator[dict[str, dict[str, SynoCamera]]], camera_id: str) -> None: ...
    @property
    def camera_data(self) -> SynoCamera: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def available(self) -> bool: ...
    @property
    def is_recording(self) -> bool: ...
    @property
    def motion_detection_enabled(self) -> bool: ...
    def camera_image(self, width: Union[int, None] = ..., height: Union[int, None] = ...) -> Union[bytes, None]: ...
    async def stream_source(self) -> Union[str, None]: ...
    def enable_motion_detection(self) -> None: ...
    def disable_motion_detection(self) -> None: ...
