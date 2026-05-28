from . import ElkM1ConfigEntry as ElkM1ConfigEntry
from .entity import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity, create_elk_entities as create_elk_entities
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from elkm1_lib.elements import Element as Element
from elkm1_lib.settings import Setting
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity
from homeassistant.const import UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ElkM1ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ElkNumberSetting(ElkAttachedEntity, NumberEntity):
    _element: Setting
    _attr_native_min_value: int
    _attr_native_max_value: int
    _attr_native_step: int
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, element: Setting, elk: Any, elk_data: ELKM1Data) -> None: ...
    _attr_native_value: Incomplete
    _attr_available: bool
    def _element_changed(self, element: Element, changeset: dict[str, Any]) -> None: ...
    async def async_set_native_value(self, value: float) -> None: ...
