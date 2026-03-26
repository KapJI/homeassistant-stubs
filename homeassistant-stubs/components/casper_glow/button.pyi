from .coordinator import CasperGlowConfigEntry as CasperGlowConfigEntry, CasperGlowCoordinator as CasperGlowCoordinator
from .entity import CasperGlowEntity as CasperGlowEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import format_mac as format_mac
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pycasperglow import CasperGlow as CasperGlow

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class CasperGlowButtonEntityDescription(ButtonEntityDescription):
    press_fn: Callable[[CasperGlow], Awaitable[None]]

BUTTON_DESCRIPTIONS: tuple[CasperGlowButtonEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: CasperGlowConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class CasperGlowButton(CasperGlowEntity, ButtonEntity):
    entity_description: CasperGlowButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: CasperGlowCoordinator, description: CasperGlowButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
