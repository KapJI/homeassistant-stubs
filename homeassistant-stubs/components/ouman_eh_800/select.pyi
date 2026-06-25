from .const import OumanDevice as OumanDevice
from .coordinator import OumanEh800ConfigEntry as OumanEh800ConfigEntry, OumanEh800Coordinator as OumanEh800Coordinator
from .entity import OumanEh800Entity as OumanEh800Entity, OumanEh800EntityDescription as OumanEh800EntityDescription
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from ouman_eh_800_api import EnumControlOumanEndpoint
from typing import override

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class OumanEh800SelectEntityDescription(OumanEh800EntityDescription, SelectEntityDescription): ...

def _select_entity(*, device: OumanDevice, key: str) -> OumanEh800SelectEntityDescription: ...

SELECT_DESCRIPTIONS: dict[EnumControlOumanEndpoint, OumanEh800SelectEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: OumanEh800ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OumanEh800SelectEntity(OumanEh800Entity, SelectEntity):
    entity_description: OumanEh800SelectEntityDescription
    _endpoint: EnumControlOumanEndpoint
    _attr_options: Incomplete
    def __init__(self, coordinator: OumanEh800Coordinator, endpoint: EnumControlOumanEndpoint, description: OumanEh800SelectEntityDescription) -> None: ...
    @property
    @override
    def current_option(self) -> str: ...
    @override
    async def async_select_option(self, option: str) -> None: ...
