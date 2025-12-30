from . import OmadaConfigEntry as OmadaConfigEntry
from .coordinator import OmadaFirmwareUpdateCoordinator as OmadaFirmwareUpdateCoordinator
from .entity import OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OmadaDeviceUpdate(OmadaDeviceEntity[OmadaFirmwareUpdateCoordinator], UpdateEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _mac: Incomplete
    _omada_client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OmadaFirmwareUpdateCoordinator, device: OmadaListDevice) -> None: ...
    def release_notes(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_in_progress: Incomplete
    @callback
    def _handle_coordinator_update(self) -> None: ...
