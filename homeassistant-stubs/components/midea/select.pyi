from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from typing import override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaSelectEntityDescription(SelectEntityDescription):
    models: list[DeviceType]
    options_attribute: str
    requires_power: bool = ...

SELECTS: list[MideaSelectEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaSelect(MideaEntity, SelectEntity):
    entity_description: MideaSelectEntityDescription
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def options(self) -> list[str]: ...
    @property
    @override
    def current_option(self) -> str | None: ...
    @override
    def select_option(self, option: str) -> None: ...
