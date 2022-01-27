from .const import DOMAIN as DOMAIN
from .data import EnergyManager as EnergyManager, async_get_manager as async_get_manager
from homeassistant.components.sensor import ATTR_LAST_RESET as ATTR_LAST_RESET, ATTR_STATE_CLASS as ATTR_STATE_CLASS, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.components.sensor.recorder import reset_detected as reset_detected
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_MEGA_WATT_HOUR as ENERGY_MEGA_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR, VOLUME_CUBIC_METERS as VOLUME_CUBIC_METERS
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id, valid_entity_id as valid_entity_id
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final, Literal

SUPPORTED_STATE_CLASSES: Any
VALID_ENERGY_UNITS: Any
VALID_ENERGY_UNITS_GAS: Any
_LOGGER: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class SourceAdapter:
    source_type: Literal['grid', 'gas']
    flow_type: Literal['flow_from', 'flow_to', None]
    stat_energy_key: Literal['stat_energy_from', 'stat_energy_to']
    entity_energy_key: Literal['entity_energy_from', 'entity_energy_to']
    total_money_key: Literal['stat_cost', 'stat_compensation']
    name_suffix: str
    entity_id_suffix: str
    def __init__(self, source_type, flow_type, stat_energy_key, entity_energy_key, total_money_key, name_suffix, entity_id_suffix) -> None: ...

SOURCE_ADAPTERS: Final[Any]

class SensorManager:
    manager: Any
    async_add_entities: Any
    current_entities: Any
    def __init__(self, manager: EnergyManager, async_add_entities: AddEntitiesCallback) -> None: ...
    async def async_start(self) -> None: ...
    async def _process_manager_data(self) -> None: ...
    def _process_sensor_data(self, adapter: SourceAdapter, config: dict, to_add: list[EnergyCostSensor], to_remove: dict[tuple[str, Union[str, None], str], EnergyCostSensor]) -> None: ...

class EnergyCostSensor(SensorEntity):
    _attr_entity_category: Any
    _wrong_state_class_reported: bool
    _wrong_unit_reported: bool
    _adapter: Any
    entity_id: Any
    _attr_device_class: Any
    _attr_state_class: Any
    _config: Any
    _last_energy_sensor_state: Any
    add_finished: Any
    def __init__(self, adapter: SourceAdapter, config: dict) -> None: ...
    _attr_native_value: float
    _attr_last_reset: Any
    def _reset(self, energy_state: State) -> None: ...
    def _update_cost(self) -> None: ...
    _attr_name: Any
    async def async_added_to_hass(self) -> None: ...
    def add_to_platform_abort(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def update_config(self, config: dict) -> None: ...
    @property
    def native_unit_of_measurement(self) -> Union[str, None]: ...
