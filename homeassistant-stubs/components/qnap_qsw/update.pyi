from .const import DOMAIN as DOMAIN, QSW_COORD_FW as QSW_COORD_FW, QSW_UPDATE as QSW_UPDATE
from .coordinator import QswFirmwareCoordinator as QswFirmwareCoordinator
from .entity import QswFirmwareEntity as QswFirmwareEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Final

UPDATE_TYPES: Final[tuple[UpdateEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class QswUpdate(QswFirmwareEntity, UpdateEntity):
    entity_description: UpdateEntityDescription
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_installed_version: Incomplete
    def __init__(self, coordinator: QswFirmwareCoordinator, description: UpdateEntityDescription, entry: ConfigEntry) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_latest_version: Incomplete
    _attr_release_summary: Incomplete
    def _async_update_attrs(self) -> None: ...
