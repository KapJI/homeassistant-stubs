from . import OmadaConfigEntry as OmadaConfigEntry
from .config_flow import CONF_SITE as CONF_SITE
from .const import DOMAIN as DOMAIN
from .coordinator import OmadaControllerStatusCoordinator as OmadaControllerStatusCoordinator, OmadaControllerUpdateCoordinator as OmadaControllerUpdateCoordinator, OmadaFirmwareUpdateCoordinator as OmadaFirmwareUpdateCoordinator
from .entity import OmadaControllerEntity as OmadaControllerEntity, OmadaDeviceEntity as OmadaDeviceEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from tplink_omada_client import OmadaControllerUpdateInfo
from tplink_omada_client.devices import OmadaListDevice as OmadaListDevice
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, config_entry: OmadaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OmadaControllerUpdate(OmadaControllerEntity, UpdateEntity):
    _attr_translation_key: str
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _update_coordinator: Incomplete
    _omada_client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, status_coordinator: OmadaControllerStatusCoordinator, update_coordinator: OmadaControllerUpdateCoordinator) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @callback
    def _handle_update_coordinator_update(self) -> None: ...
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
    @property
    def _update_data(self) -> OmadaControllerUpdateInfo | None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_supported_features: Incomplete
    def _update_attrs(self) -> None: ...
    @override
    def release_notes(self) -> str | None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...

class OmadaDeviceUpdate(OmadaDeviceEntity[OmadaFirmwareUpdateCoordinator], UpdateEntity):
    _attr_supported_features: Incomplete
    _attr_device_class: Incomplete
    _mac: Incomplete
    _omada_client: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: OmadaFirmwareUpdateCoordinator, device: OmadaListDevice) -> None: ...
    @override
    def release_notes(self) -> str | None: ...
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    _attr_in_progress: Incomplete
    @callback
    @override
    def _handle_coordinator_update(self) -> None: ...
