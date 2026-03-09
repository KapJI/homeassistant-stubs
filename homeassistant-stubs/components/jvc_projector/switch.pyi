from .coordinator import JVCConfigEntry as JVCConfigEntry, JvcProjectorDataUpdateCoordinator as JvcProjectorDataUpdateCoordinator
from .entity import JvcProjectorEntity as JvcProjectorEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from jvcprojector import Command as Command
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class JvcProjectorSwitchDescription(SwitchEntityDescription):
    command: type[Command]

SWITCHES: Final[tuple[JvcProjectorSwitchDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: JVCConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class JvcProjectorSwitchEntity(JvcProjectorEntity, SwitchEntity):
    command: type[Command]
    entity_description: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: JvcProjectorDataUpdateCoordinator, description: JvcProjectorSwitchDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
