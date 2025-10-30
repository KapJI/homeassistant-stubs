from .coordinator import ToloConfigEntry as ToloConfigEntry, ToloSaunaUpdateCoordinator as ToloSaunaUpdateCoordinator
from .entity import ToloSaunaCoordinatorEntity as ToloSaunaCoordinatorEntity
from _typeshed import Incomplete
from homeassistant.components.fan import FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ToloConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ToloFan(ToloSaunaCoordinatorEntity, FanEntity):
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ToloSaunaUpdateCoordinator, entry: ToloConfigEntry) -> None: ...
    @property
    def is_on(self) -> bool: ...
    def turn_on(self, percentage: int | None = None, preset_mode: str | None = None, **kwargs: Any) -> None: ...
    def turn_off(self, **kwargs: Any) -> None: ...
