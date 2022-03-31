from .coordinator import SteamistDataUpdateCoordinator as SteamistDataUpdateCoordinator
from aiosteamist import SteamistStatus as SteamistStatus
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_MODEL as CONF_MODEL, CONF_NAME as CONF_NAME
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

class SteamistEntity(CoordinatorEntity[SteamistDataUpdateCoordinator], Entity):
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    _attr_device_info: Any
    def __init__(self, coordinator: SteamistDataUpdateCoordinator, entry: ConfigEntry, description: EntityDescription) -> None: ...
    @property
    def _status(self) -> SteamistStatus: ...
