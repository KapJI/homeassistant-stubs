from .const import ATTR_ROUTERBOARD_FIRMWARE as ATTR_ROUTERBOARD_FIRMWARE, ATTR_SYSTEM_FIRMWARE as ATTR_SYSTEM_FIRMWARE, BACKUP as BACKUP, MIKROTIK_SERVICES as MIKROTIK_SERVICES, ROUTERBOARD as ROUTERBOARD, UPDATE as UPDATE
from .coordinator import MikrotikConfigEntry as MikrotikConfigEntry, mikrotik_config_entry_errors as mikrotik_config_entry_errors
from .entity import MikrotikEntity as MikrotikEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class MikrotikUpdateEntityDescription(UpdateEntityDescription):
    release_notes: str | None = ...
    supported_features: UpdateEntityFeature
    path: str
    installed_version: str
    latest_version: str

UPDATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: MikrotikConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MikrotikUpdateEntity(MikrotikEntity, UpdateEntity):
    entity_description: MikrotikUpdateEntityDescription
    @property
    @override
    def supported_features(self) -> UpdateEntityFeature: ...
    @property
    def _device_path_info(self) -> dict[str, Any]: ...
    @property
    @override
    def installed_version(self) -> str | None: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
    @property
    @override
    def release_url(self) -> str | None: ...
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
