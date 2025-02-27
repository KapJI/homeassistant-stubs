from . import TPLinkConfigEntry as TPLinkConfigEntry, legacy_device_id as legacy_device_id
from .const import DOMAIN as DOMAIN
from .coordinator import TPLinkDataUpdateCoordinator as TPLinkDataUpdateCoordinator
from .entity import CoordinatedTPLinkModuleEntity as CoordinatedTPLinkModuleEntity, TPLinkModuleEntityDescription as TPLinkModuleEntityDescription, async_refresh_after as async_refresh_after
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.siren import ATTR_DURATION as ATTR_DURATION, ATTR_TONE as ATTR_TONE, ATTR_VOLUME_LEVEL as ATTR_VOLUME_LEVEL, SirenEntity as SirenEntity, SirenEntityDescription as SirenEntityDescription, SirenEntityFeature as SirenEntityFeature, SirenTurnOnServiceParameters as SirenTurnOnServiceParameters
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from kasa import Device as Device
from typing import Any

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class TPLinkSirenEntityDescription(SirenEntityDescription, TPLinkModuleEntityDescription):
    unique_id_fn: Callable[[Device, TPLinkModuleEntityDescription], str] = ...

SIREN_DESCRIPTIONS: tuple[TPLinkSirenEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: TPLinkConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TPLinkSirenEntity(CoordinatedTPLinkModuleEntity, SirenEntity):
    _attr_name: Incomplete
    _attr_supported_features: Incomplete
    entity_description: TPLinkSirenEntityDescription
    _alarm_module: Incomplete
    _alarm_volume_max: Incomplete
    _alarm_duration_max: Incomplete
    def __init__(self, device: Device, coordinator: TPLinkDataUpdateCoordinator, description: TPLinkSirenEntityDescription, *, parent: Device | None = None) -> None: ...
    @async_refresh_after
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @async_refresh_after
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_is_on: Incomplete
    _attr_available_tones: Incomplete
    @callback
    def _async_update_attrs(self) -> bool: ...
