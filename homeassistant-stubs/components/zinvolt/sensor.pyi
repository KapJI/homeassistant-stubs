from .coordinator import ZinvoltConfigEntry as ZinvoltConfigEntry, ZinvoltDeviceCoordinator as ZinvoltDeviceCoordinator
from .entity import ZinvoltEntity as ZinvoltEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import PERCENTAGE as PERCENTAGE, UnitOfPower as UnitOfPower
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from zinvolt.models import BatteryState as BatteryState

@dataclass(kw_only=True, frozen=True)
class ZinvoltBatteryStateDescription(SensorEntityDescription):
    value_fn: Callable[[BatteryState], float]

SENSORS: tuple[ZinvoltBatteryStateDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ZinvoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZinvoltBatteryStateSensor(ZinvoltEntity, SensorEntity):
    entity_description: ZinvoltBatteryStateDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator, description: ZinvoltBatteryStateDescription) -> None: ...
    @property
    def native_value(self) -> float: ...
