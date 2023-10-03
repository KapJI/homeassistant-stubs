from . import ElkAttachedEntity as ElkAttachedEntity, ElkEntity as ElkEntity
from .const import DOMAIN as DOMAIN
from .models import ELKM1Data as ELKM1Data
from _typeshed import Incomplete
from elkm1_lib.elements import Element as Element
from elkm1_lib.zones import Zone as Zone
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ElkBinarySensor(ElkAttachedEntity, BinarySensorEntity):
    _element: Zone
    _attr_entity_registry_enabled_default: bool
    _attr_is_on: Incomplete
    def _element_changed(self, _: Element, changeset: Any) -> None: ...
