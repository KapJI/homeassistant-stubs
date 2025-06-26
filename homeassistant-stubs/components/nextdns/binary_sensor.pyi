from . import NextDnsConfigEntry as NextDnsConfigEntry
from .entity import NextDnsEntity as NextDnsEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from nextdns import ConnectionStatus as ConnectionStatus

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NextDnsBinarySensorEntityDescription(BinarySensorEntityDescription):
    state: Callable[[ConnectionStatus, str], bool]

SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NextDnsBinarySensor(NextDnsEntity, BinarySensorEntity):
    entity_description: NextDnsBinarySensorEntityDescription
    @property
    def is_on(self) -> bool: ...
