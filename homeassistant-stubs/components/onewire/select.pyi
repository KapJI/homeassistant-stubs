from .const import READ_MODE_INT as READ_MODE_INT
from .entity import OneWireEntity as OneWireEntity, OneWireEntityDescription as OneWireEntityDescription
from .onewirehub import OWDeviceDescription as OWDeviceDescription, OneWireConfigEntry as OneWireConfigEntry, OneWireHub as OneWireHub, SIGNAL_NEW_DEVICE_CONNECTED as SIGNAL_NEW_DEVICE_CONNECTED
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete

@dataclass(frozen=True)
class OneWireSelectEntityDescription(OneWireEntityDescription, SelectEntityDescription): ...

ENTITY_DESCRIPTIONS: dict[str, tuple[OneWireEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: OneWireConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def get_entities(onewire_hub: OneWireHub, devices: list[OWDeviceDescription]) -> list[OneWireSelectEntity]: ...

class OneWireSelectEntity(OneWireEntity, SelectEntity):
    entity_description: OneWireSelectEntityDescription
    @property
    def current_option(self) -> str | None: ...
    def select_option(self, option: str) -> None: ...
