from .const import DOMAIN as DOMAIN
from .coordinator import ConsoleData as ConsoleData, XboxUpdateCoordinator as XboxUpdateCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from pythonxbox.api.provider.people.models import Person as Person
from pythonxbox.api.provider.smartglass.models import SmartglassConsole as SmartglassConsole
from pythonxbox.api.provider.titlehub.models import Title as Title
from typing import Any

MAP_MODEL: Incomplete

@dataclass(kw_only=True, frozen=True)
class XboxBaseEntityDescription(EntityDescription):
    entity_picture_fn: Callable[[Person, Title | None], str | None] | None = ...
    attributes_fn: Callable[[Person, Title | None], Mapping[str, Any] | None] | None = ...
    deprecated: bool | None = ...

class XboxBaseEntity(CoordinatorEntity[XboxUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: XboxBaseEntityDescription
    xuid: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: XboxUpdateCoordinator, xuid: str, entity_description: XboxBaseEntityDescription) -> None: ...
    @property
    def data(self) -> Person: ...
    @property
    def title_info(self) -> Title | None: ...
    @property
    def entity_picture(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, float | None] | None: ...

class XboxConsoleBaseEntity(CoordinatorEntity[XboxUpdateCoordinator]):
    _attr_has_entity_name: bool
    client: Incomplete
    _console: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, console: SmartglassConsole, coordinator: XboxUpdateCoordinator) -> None: ...
    @property
    def data(self) -> ConsoleData: ...

def check_deprecated_entity(hass: HomeAssistant, xuid: str, entity_description: XboxBaseEntityDescription, entity_domain: str) -> bool: ...
def to_https(image_url: str) -> str: ...
def profile_pic(person: Person, _: Title | None = None) -> str | None: ...
