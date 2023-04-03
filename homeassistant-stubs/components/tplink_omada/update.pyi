from .const import DOMAIN as DOMAIN
from .controller import OmadaSiteController as OmadaSiteController
from .coordinator import OmadaCoordinator as OmadaCoordinator
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from tplink_omada_client.devices import OmadaFirmwareUpdate as OmadaFirmwareUpdate, OmadaListDevice as OmadaListDevice
from tplink_omada_client.omadasiteclient import OmadaSiteClient as OmadaSiteClient
from typing import Any, NamedTuple

POLL_DELAY_IDLE: Incomplete
POLL_DELAY_UPGRADE: int

class FirmwareUpdateStatus(NamedTuple):
    device: OmadaListDevice
    firmware: OmadaFirmwareUpdate | None

class OmadaFirmwareUpdateCoodinator(OmadaCoordinator[FirmwareUpdateStatus]):
    def __init__(self, hass: HomeAssistant, omada_client: OmadaSiteClient) -> None: ...
    update_interval: Incomplete
    async def _get_firmware_updates(self) -> list[FirmwareUpdateStatus]: ...
    async def poll_update(self) -> dict[str, FirmwareUpdateStatus]: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OmadaDeviceUpdate(OmadaDeviceEntity[FirmwareUpdateStatus], UpdateEntity):
    _attr_supported_features: Incomplete
    _attr_has_entity_name: bool
    _attr_name: str
    _mac: Incomplete
    _omada_client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OmadaFirmwareUpdateCoodinator, device: OmadaListDevice) -> None: ...
    def release_notes(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_in_progress: Incomplete
    def _handle_coordinator_update(self) -> None: ...
