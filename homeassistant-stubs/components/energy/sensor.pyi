import asyncio
from .const import DOMAIN as DOMAIN
from .data import EnergyManager as EnergyManager, PowerConfig as PowerConfig, async_get_manager as async_get_manager
from .helpers import generate_power_sensor_entity_id as generate_power_sensor_entity_id, generate_power_sensor_unique_id as generate_power_sensor_unique_id
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.sensor import ATTR_LAST_RESET as ATTR_LAST_RESET, ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.components.sensor.recorder import reset_detected as reset_detected
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, UnitOfEnergy as UnitOfEnergy, UnitOfPower as UnitOfPower, UnitOfVolume as UnitOfVolume
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util import unit_conversion as unit_conversion
from homeassistant.util.unit_system import METRIC_SYSTEM as METRIC_SYSTEM
from typing import Any, Final, Literal

SUPPORTED_STATE_CLASSES: Incomplete
VALID_ENERGY_UNITS: set[str]
VALID_ENERGY_UNITS_GAS: Incomplete
VALID_VOLUME_UNITS_WATER: set[str]
_LOGGER: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

@dataclass(slots=True)
class SourceAdapter:
    source_type: Literal['grid', 'gas', 'water']
    flow_type: Literal['flow_from', 'flow_to'] | None
    stat_energy_key: Literal['stat_energy_from', 'stat_energy_to']
    total_money_key: Literal['stat_cost', 'stat_compensation']
    name_suffix: str
    entity_id_suffix: str

SOURCE_ADAPTERS: Final[Incomplete]

class EntityNotFoundError(HomeAssistantError): ...

class SensorManager:
    manager: Incomplete
    async_add_entities: Incomplete
    current_entities: dict[tuple[str, str | None, str], EnergyCostSensor]
    current_power_entities: dict[str, EnergyPowerSensor]
    def __init__(self, manager: EnergyManager, async_add_entities: AddEntitiesCallback) -> None: ...
    async def async_start(self) -> None: ...
    async def _process_manager_data(self) -> None: ...
    @callback
    def _process_sensor_data(self, adapter: SourceAdapter, config: Mapping[str, Any], to_add: list[EnergyCostSensor | EnergyPowerSensor], to_remove: dict[tuple[str, str | None, str], EnergyCostSensor]) -> None: ...
    @callback
    def _process_power_sensor_data(self, energy_source: Mapping[str, Any], to_add: list[EnergyCostSensor | EnergyPowerSensor], to_remove: dict[str, EnergyPowerSensor]) -> None: ...
    @staticmethod
    def _needs_power_sensor(power_config: PowerConfig) -> bool: ...
    def _create_or_keep_power_sensor(self, source_type: str, power_config: PowerConfig, to_add: list[EnergyCostSensor | EnergyPowerSensor], to_remove: dict[str, EnergyPowerSensor]) -> None: ...

def _set_result_unless_done(future: asyncio.Future[None]) -> None: ...

class EnergyCostSensor(SensorEntity):
    _attr_entity_registry_visible_default: bool
    _attr_should_poll: bool
    _wrong_state_class_reported: bool
    _wrong_unit_reported: bool
    _adapter: Incomplete
    entity_id: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _config: Incomplete
    _last_energy_sensor_state: State | None
    add_finished: asyncio.Future[None]
    def __init__(self, adapter: SourceAdapter, config: Mapping[str, Any]) -> None: ...
    _attr_native_value: float
    _attr_last_reset: Incomplete
    def _reset(self, energy_state: State) -> None: ...
    @callback
    def _update_cost(self) -> None: ...
    def _get_energy_price(self, valid_units: set[str], default_unit: str | None) -> tuple[float, str | None]: ...
    def _convert_energy_price(self, energy_price: float, energy_price_unit: str | None, energy_unit: str) -> float: ...
    _attr_name: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_state_changed_listener(self, *_: Any) -> None: ...
    @callback
    def add_to_platform_abort(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @callback
    def update_config(self, config: Mapping[str, Any]) -> None: ...
    @property
    def native_unit_of_measurement(self) -> str | None: ...
    @property
    def unique_id(self) -> str | None: ...

class EnergyPowerSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_has_entity_name: bool
    _source_type: Incomplete
    _config: PowerConfig
    _attr_unique_id: Incomplete
    entity_id: Incomplete
    _source_sensors: list[str]
    _is_inverted: Incomplete
    _is_combined: Incomplete
    add_finished: asyncio.Future[None]
    def __init__(self, source_type: str, config: PowerConfig, unique_id: str, entity_id: str) -> None: ...
    @property
    def available(self) -> bool: ...
    _attr_native_value: Incomplete
    @callback
    def _update_state(self) -> None: ...
    _attr_native_unit_of_measurement: Incomplete
    _attr_name: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @callback
    def _async_state_changed_listener(self, *_: Any) -> None: ...
    @callback
    def add_to_platform_abort(self) -> None: ...
