from . import NextDnsConfigEntry as NextDnsConfigEntry
from .const import ATTR_DNSSEC as ATTR_DNSSEC, ATTR_ENCRYPTION as ATTR_ENCRYPTION, ATTR_IP_VERSIONS as ATTR_IP_VERSIONS, ATTR_PROTOCOLS as ATTR_PROTOCOLS, ATTR_STATUS as ATTR_STATUS
from .entity import NextDnsEntity as NextDnsEntity
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from nextdns.model import NextDnsData as NextDnsData

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class NextDnsSensorEntityDescription[CoordinatorDataT: NextDnsData](SensorEntityDescription):
    coordinator_type: str
    value: Callable[[CoordinatorDataT], StateType]

SENSORS: tuple[NextDnsSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: NextDnsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NextDnsSensor[CoordinatorDataT: NextDnsData](NextDnsEntity[CoordinatorDataT], SensorEntity):
    entity_description: NextDnsSensorEntityDescription[CoordinatorDataT]
    @property
    def native_value(self) -> StateType: ...
