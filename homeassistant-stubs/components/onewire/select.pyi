from .entity import OneWireEntity as OneWireEntity
from .onewirehub import OWDeviceDescription as OWDeviceDescription, OneWireConfigEntry as OneWireConfigEntry, OneWireHub as OneWireHub, SIGNAL_NEW_DEVICE_CONNECTED as SIGNAL_NEW_DEVICE_CONNECTED
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
SCAN_INTERVAL: Incomplete
ENTITY_DESCRIPTIONS: dict[str, tuple[SelectEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, config_entry: OneWireConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def get_entities(onewire_hub: OneWireHub, devices: list[OWDeviceDescription]) -> list[OneWireSelectEntity]: ...

class OneWireSelectEntity(OneWireEntity, SelectEntity):
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
