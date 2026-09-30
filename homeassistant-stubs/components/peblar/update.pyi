from .const import DOMAIN as DOMAIN
from .coordinator import PeblarConfigEntry as PeblarConfigEntry, PeblarVersionDataUpdateCoordinator as PeblarVersionDataUpdateCoordinator, PeblarVersionInformation as PeblarVersionInformation
from .entity import PeblarEntity as PeblarEntity
from .helpers import peblar_exception_handler as peblar_exception_handler
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from peblar import PackageType
from typing import Any, override

PARALLEL_UPDATES: int

def _customization_update_pending(versions: PeblarVersionInformation) -> bool: ...

@dataclass(frozen=True, kw_only=True)
class PeblarUpdateEntityDescription(UpdateEntityDescription):
    available_fn: Callable[[PeblarVersionInformation], str | None]
    has_fn: Callable[[PeblarVersionInformation], bool] = ...
    installed_fn: Callable[[PeblarVersionInformation], str | None]
    package_type: PackageType

DESCRIPTIONS: tuple[PeblarUpdateEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PeblarConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PeblarUpdateEntity(PeblarEntity[PeblarVersionDataUpdateCoordinator], UpdateEntity):
    entity_description: PeblarUpdateEntityDescription
    _attr_supported_features: Incomplete
    @property
    @override
    def in_progress(self) -> bool: ...
    @property
    @override
    def installed_version(self) -> str | None: ...
    @property
    @override
    def latest_version(self) -> str | None: ...
    @peblar_exception_handler
    @override
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...
    async def _async_raise_if_customization_pending(self) -> None: ...
