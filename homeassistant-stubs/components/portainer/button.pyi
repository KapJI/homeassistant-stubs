from . import PortainerConfigEntry as PortainerConfigEntry
from .const import DOMAIN as DOMAIN
from .coordinator import PortainerContainerData as PortainerContainerData, PortainerCoordinator as PortainerCoordinator, PortainerCoordinatorData as PortainerCoordinatorData
from .entity import PortainerContainerEntity as PortainerContainerEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pyportainer import Portainer as Portainer
from typing import Any

@dataclass(frozen=True, kw_only=True)
class PortainerButtonDescription(ButtonEntityDescription):
    press_action: Callable[[Portainer, int, str], Coroutine[Any, Any, None]]

BUTTONS: tuple[PortainerButtonDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: PortainerConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class PortainerButton(PortainerContainerEntity, ButtonEntity):
    entity_description: PortainerButtonDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: PortainerCoordinator, entity_description: PortainerButtonDescription, device_info: PortainerContainerData, via_device: PortainerCoordinatorData) -> None: ...
    async def async_press(self) -> None: ...
