from .coordinator import SystemNexa2ConfigEntry as SystemNexa2ConfigEntry, SystemNexa2DataUpdateCoordinator as SystemNexa2DataUpdateCoordinator
from .entity import SystemNexa2Entity as SystemNexa2Entity
from _typeshed import Incomplete
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: SystemNexa2ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SystemNexa2Light(SystemNexa2Entity, LightEntity):
    _attr_translation_key: str
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    def __init__(self, coordinator: SystemNexa2DataUpdateCoordinator) -> None: ...
    @override
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_on(self) -> bool | None: ...
    @property
    @override
    def brightness(self) -> int | None: ...
