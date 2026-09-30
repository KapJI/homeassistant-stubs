from .const import DOMAIN as DOMAIN
from .coordinator import VitesyConfigEntry as VitesyConfigEntry, VitesyDataUpdateCoordinator as VitesyDataUpdateCoordinator
from .entity import VitesyEntity as VitesyEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VitesyButtonEntityDescription(ButtonEntityDescription):
    component: str

BUTTONS: tuple[VitesyButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: VitesyConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VitesyButton(VitesyEntity, ButtonEntity):
    entity_description: VitesyButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VitesyDataUpdateCoordinator, device_id: str, description: VitesyButtonEntityDescription) -> None: ...
    @override
    async def async_press(self) -> None: ...
