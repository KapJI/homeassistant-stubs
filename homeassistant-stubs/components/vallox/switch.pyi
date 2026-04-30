from .coordinator import ValloxConfigEntry as ValloxConfigEntry, ValloxDataUpdateCoordinator as ValloxDataUpdateCoordinator
from .entity import ValloxEntity as ValloxEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME, EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

class ValloxSwitchEntity(ValloxEntity, SwitchEntity):
    entity_description: ValloxSwitchEntityDescription
    _attr_entity_category: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, name: str, coordinator: ValloxDataUpdateCoordinator, description: ValloxSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def _set_value(self, value: bool) -> None: ...

@dataclass(frozen=True, kw_only=True)
class ValloxSwitchEntityDescription(SwitchEntityDescription):
    metric_key: str

SWITCH_ENTITIES: tuple[ValloxSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ValloxConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
