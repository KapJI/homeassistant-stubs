import abc
from . import AirzoneCloudConfigEntry as AirzoneCloudConfigEntry
from .coordinator import AirzoneUpdateCoordinator as AirzoneUpdateCoordinator
from .entity import AirzoneEntity as AirzoneEntity, AirzoneZoneEntity as AirzoneZoneEntity
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.switch import SwitchDeviceClass as SwitchDeviceClass, SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Final

@dataclass(frozen=True, kw_only=True)
class AirzoneSwitchDescription(SwitchEntityDescription):
    api_param: str

ZONE_SWITCH_TYPES: Final[tuple[AirzoneSwitchDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: AirzoneCloudConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AirzoneBaseSwitch(AirzoneEntity, SwitchEntity, metaclass=abc.ABCMeta):
    entity_description: AirzoneSwitchDescription
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_attrs(self) -> None: ...

class AirzoneZoneSwitch(AirzoneZoneEntity, AirzoneBaseSwitch):
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    entity_description: Incomplete
    def __init__(self, coordinator: AirzoneUpdateCoordinator, description: AirzoneSwitchDescription, zone_id: str, zone_data: dict[str, Any]) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
