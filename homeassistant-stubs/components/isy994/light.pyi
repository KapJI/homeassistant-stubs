from .const import CONF_RESTORE_LIGHT_STATE as CONF_RESTORE_LIGHT_STATE, UOM_PERCENTAGE as UOM_PERCENTAGE, _LOGGER as _LOGGER
from .entity import ISYNodeEntity as ISYNodeEntity
from .models import IsyConfigEntry as IsyConfigEntry
from _typeshed import Incomplete
from homeassistant.components.light import ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from pyisy.helpers import NodeProperty as NodeProperty
from pyisy.nodes import Node as Node
from typing import Any, override

ATTR_LAST_BRIGHTNESS: str

async def async_setup_entry(hass: HomeAssistant, entry: IsyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ISYLightEntity(ISYNodeEntity, LightEntity, RestoreEntity):
    _attr_color_mode: Incomplete
    _attr_supported_color_modes: Incomplete
    _last_brightness: int | None
    _restore_light_state: Incomplete
    def __init__(self, node: Node, restore_light_state: bool, device_info: DeviceInfo | None = None) -> None: ...
    @property
    @override
    def is_on(self) -> bool: ...
    @property
    @override
    def brightness(self) -> int | None: ...
    @override
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    @override
    def async_on_update(self, event: NodeProperty) -> None: ...
    @override
    async def async_turn_on(self, brightness: int | None = None, **kwargs: Any) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any]: ...
    @override
    async def async_added_to_hass(self) -> None: ...
