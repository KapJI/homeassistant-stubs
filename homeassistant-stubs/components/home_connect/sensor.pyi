from .common import setup_home_connect_entry as setup_home_connect_entry
from .const import APPLIANCES_WITH_PROGRAMS as APPLIANCES_WITH_PROGRAMS, BSH_OPERATION_STATE_FINISHED as BSH_OPERATION_STATE_FINISHED, BSH_OPERATION_STATE_PAUSE as BSH_OPERATION_STATE_PAUSE, BSH_OPERATION_STATE_RUN as BSH_OPERATION_STATE_RUN, UNIT_MAP as UNIT_MAP
from .coordinator import HomeConnectApplianceData as HomeConnectApplianceData, HomeConnectConfigEntry as HomeConnectConfigEntry
from .entity import HomeConnectEntity as HomeConnectEntity, constraint_fetcher as constraint_fetcher
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfVolume as UnitOfVolume
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util import slugify as slugify

_LOGGER: Incomplete
PARALLEL_UPDATES: int
EVENT_OPTIONS: Incomplete

@dataclass(frozen=True, kw_only=True)
class HomeConnectSensorEntityDescription(SensorEntityDescription):
    appliance_types: tuple[str, ...] | None = ...
    fetch_unit: bool = ...

BSH_PROGRAM_SENSORS: Incomplete
SENSORS: Incomplete
EVENT_SENSORS: Incomplete

def _get_entities_for_appliance(entry: HomeConnectConfigEntry, appliance: HomeConnectApplianceData) -> list[HomeConnectEntity]: ...
def _add_event_sensor_entity(entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, appliance: HomeConnectApplianceData, description: HomeConnectSensorEntityDescription, remove_event_sensor_listener_list: list[Callable[[], None]]) -> None: ...
def _add_event_sensor_listeners(entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback, remove_event_sensor_listener_dict: dict[str, list[CALLBACK_TYPE]]) -> None: ...
def _remove_event_sensor_listeners_on_depaired(entry: HomeConnectConfigEntry, remove_event_sensor_listener_dict: dict[str, list[CALLBACK_TYPE]]) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: HomeConnectConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HomeConnectSensor(HomeConnectEntity, SensorEntity):
    entity_description: HomeConnectSensorEntityDescription
    def update_native_value(self) -> None: ...
    _attr_native_value: Incomplete
    def _update_native_value(self, status: str | float) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @constraint_fetcher
    async def fetch_unit(self) -> None: ...

class HomeConnectProgramSensor(HomeConnectSensor):
    program_running: bool
    async def async_added_to_hass(self) -> None: ...
    _attr_native_value: Incomplete
    @callback
    def _handle_operation_state_event(self) -> None: ...
    @property
    def available(self) -> bool: ...
    def update_native_value(self) -> None: ...

class HomeConnectEventSensor(HomeConnectSensor):
    def update_native_value(self) -> None: ...
