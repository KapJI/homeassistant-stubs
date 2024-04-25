from .dashboard import ESPHomeDashboard as ESPHomeDashboard, async_get_dashboard as async_get_dashboard
from .domain_data import DomainData as DomainData
from .entry_data import RuntimeEntryData as RuntimeEntryData
from _typeshed import Incomplete
from aioesphomeapi import DeviceInfo as ESPHomeDeviceInfo, EntityInfo as EntityInfo
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

KEY_UPDATE_LOCK: str
NO_FEATURES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ESPHomeUpdateEntity(CoordinatorEntity[ESPHomeDashboard], UpdateEntity):
    _attr_has_entity_name: bool
    _attr_device_class: Incomplete
    _attr_title: str
    _attr_name: str
    _attr_release_url: str
    _entry_data: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry_data: RuntimeEntryData, coordinator: ESPHomeDashboard) -> None: ...
    _attr_supported_features: Incomplete
    _attr_installed_version: Incomplete
    _attr_latest_version: Incomplete
    def _update_attrs(self) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    @property
    def _device_info(self) -> ESPHomeDeviceInfo: ...
    @property
    def available(self) -> bool: ...
    def _handle_device_update(self, static_info: list[EntityInfo] | None = None) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
