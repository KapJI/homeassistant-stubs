from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from _typeshed import Incomplete
from datetime import time as dt_time
from elkm1_lib.elements import Element as Element
from elkm1_lib.settings import Setting
from homeassistant.components.time import TimeEntity as TimeEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElkTimeSetting(ElkAttachedEntity, TimeEntity):
    _element: Setting
    _attr_native_value: Incomplete
    _attr_available: bool
    def _element_changed(self, element: Element, changeset: dict[str, Any]) -> None: ...
    async def async_set_value(self, value: dt_time) -> None: ...
