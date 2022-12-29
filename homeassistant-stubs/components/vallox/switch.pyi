from . import ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator, ValloxEntity as ValloxEntity
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from vallox_websocket_api import Vallox as Vallox

class ValloxSwitchEntity(ValloxEntity, SwitchEntity):
    entity_description: ValloxSwitchEntityDescription
    _attr_entity_category: Incomplete
    _attr_has_entity_name: bool
    _attr_unique_id: Incomplete
    _client: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxSwitchEntityDescription, client: Vallox) -> None: ...
    @property
    def is_on(self) -> Union[bool, None]: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _set_value(self, value: bool) -> None: ...

class ValloxMetricKeyMixin:
    metric_key: str
    def __init__(self, metric_key) -> None: ...

class ValloxSwitchEntityDescription(SwitchEntityDescription, ValloxMetricKeyMixin):
    def __init__(self, metric_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SWITCH_ENTITIES: tuple[ValloxSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
