from .const import DOMAIN as DOMAIN
from .coordinator import WattwaechterConfigEntry as WattwaechterConfigEntry, WattwaechterCoordinator as WattwaechterCoordinator
from .entity import WattwaechterEntity as WattwaechterEntity
from _typeshed import Incomplete
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: WattwaechterConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class WattwaechterUpdateEntity(WattwaechterEntity, UpdateEntity):
    _attr_device_class: Incomplete
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: WattwaechterCoordinator) -> None: ...
    @property
    @override
    def installed_version(self) -> str | None: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
    @override
    def release_notes(self) -> str | None: ...
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
