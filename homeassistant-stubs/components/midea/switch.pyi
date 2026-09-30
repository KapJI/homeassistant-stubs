from .entity import MideaConfigEntry as MideaConfigEntry, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from midealocal.const import DeviceType
from typing import Any, override

PARALLEL_UPDATES: int

@dataclass(kw_only=True, frozen=True)
class MideaSwitchEntityDescription(SwitchEntityDescription):
    models: list[DeviceType]
    capability: str | None = ...

SWITCHES: list[MideaSwitchEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaSwitch(MideaEntity, SwitchEntity):
    entity_description: MideaSwitchEntityDescription
    @property
    @override
    def is_on(self) -> bool | None: ...
    @override
    def turn_on(self, **kwargs: Any) -> None: ...
    @override
    def turn_off(self, **kwargs: Any) -> None: ...
