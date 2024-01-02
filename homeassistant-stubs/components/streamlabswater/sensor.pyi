from . import StreamlabsCoordinator as StreamlabsCoordinator
from .const import DOMAIN as DOMAIN
from .coordinator import StreamlabsData as StreamlabsData
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

NAME_DAILY_USAGE: str
NAME_MONTHLY_USAGE: str
NAME_YEARLY_USAGE: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class StreamLabsDailyUsage(CoordinatorEntity[StreamlabsCoordinator], SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _location_id: Incomplete
    def __init__(self, coordinator: StreamlabsCoordinator, location_id: str) -> None: ...
    @property
    def location_data(self) -> StreamlabsData: ...
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> float: ...

class StreamLabsMonthlyUsage(StreamLabsDailyUsage):
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> float: ...

class StreamLabsYearlyUsage(StreamLabsDailyUsage):
    @property
    def name(self) -> str: ...
    @property
    def native_value(self) -> float: ...
