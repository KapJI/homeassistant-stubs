from .const import DOMAIN as DOMAIN
from .data import EnergyManager as EnergyManager, async_get_manager as async_get_manager
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import ATTR_LAST_RESET as ATTR_LAST_RESET, ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.components.sensor.recorder import reset_detected as reset_detected
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, UnitOfEnergy as UnitOfEnergy, UnitOfVolume as UnitOfVolume, VOLUME_CUBIC_FEET as VOLUME_CUBIC_FEET, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS, VOLUME_GALLONS as VOLUME_GALLONS, VOLUME_LITERS as VOLUME_LITERS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import unit_conversion as unit_conversion
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Final, Literal

SUPPORTED_STATE_CLASSES: Incomplete
VALID_ENERGY_UNITS: set[str]
VALID_ENERGY_UNITS_GAS: Incomplete
VALID_VOLUME_UNITS_WATER: Incomplete
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class SourceAdapter:
    source_type: Literal['grid', 'gas', 'water']
    flow_type: Literal['flow_from', 'flow_to', None]
    stat_energy_key: Literal['stat_energy_from', 'stat_energy_to']
    total_money_key: Literal['stat_cost', 'stat_compensation']
    name_suffix: str
    entity_id_suffix: str
    def __init__(self, source_type, flow_type, stat_energy_key, total_money_key, name_suffix, entity_id_suffix) -> None: ...

SOURCE_ADAPTERS: Final[Incomplete]

class SensorManager:
    manager: Incomplete
    async_add_entities: Incomplete
    current_entities: Incomplete
    def __init__(self, manager: EnergyManager, async_add_entities: AddEntitiesCallback) -> None: ...
    async def async_start(self) -> None: ...
    async def _process_manager_data(self) -> None: ...
    def _process_sensor_data(self, adapter: SourceAdapter, config: dict, to_add: list[EnergyCostSensor], to_remove: dict[tuple[str, Union[str, None], str], EnergyCostSensor]) -> None: ...

class EnergyCostSensor(SensorEntity):
    _attr_entity_registry_visible_default: bool
    _wrong_state_class_reported: bool
    _wrong_unit_reported: bool
    _adapter: Incomplete
    entity_id: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _config: Incomplete
    _last_energy_sensor_state: Incomplete
    add_finished: Incomplete
    def __init__(self, adapter: SourceAdapter, config: dict) -> None: ...
    _attr_native_value: float
    _attr_last_reset: Incomplete
    def _reset(self, energy_state: State) -> None: ...
    def _update_cost(self) -> None: ...
    _attr_name: Incomplete
    async def async_added_to_hass(self) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def update_config(self, config: dict) -> None: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
