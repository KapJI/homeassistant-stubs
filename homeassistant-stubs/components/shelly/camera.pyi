from .coordinator import ShellyConfigEntry as ShellyConfigEntry, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import RpcEntityDescription as RpcEntityDescription, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import get_host as get_host
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.camera import Camera as Camera, CameraEntityDescription as CameraEntityDescription, CameraEntityFeature as CameraEntityFeature
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class RpcCameraEntityDescription(RpcEntityDescription, CameraEntityDescription):
    stream: int

RPC_CAMERA_ENTITIES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ShellyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ShellyCameraEntity(ShellyRpcAttributeEntity, Camera):
    _attr_brand: str
    _attr_supported_features: Incomplete
    entity_description: RpcCameraEntityDescription
    _attr_model: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcCameraEntityDescription) -> None: ...
    @override
    @property
    def available(self) -> bool: ...
    @override
    @property
    def is_on(self) -> bool: ...
    @override
    @property
    def is_recording(self) -> bool: ...
    @override
    @property
    def is_streaming(self) -> bool: ...
    @override
    async def stream_source(self) -> str | None: ...
    @override
    @property
    def use_stream_for_stills(self) -> bool: ...
