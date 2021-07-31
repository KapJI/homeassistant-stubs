from .const import DOMAIN as DOMAIN
from .data import EnergyManager as EnergyManager, async_get_manager as async_get_manager
from homeassistant.components.sensor import ATTR_LAST_RESET as ATTR_LAST_RESET, DEVICE_CLASS_MONETARY as DEVICE_CLASS_MONETARY, STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, SensorEntity as SensorEntity
from homeassistant.const import ATTR_UNIT_OF_MEASUREMENT as ATTR_UNIT_OF_MEASUREMENT, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENERGY_WATT_HOUR as ENERGY_WATT_HOUR
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback, split_entity_id as split_entity_id
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, Final, Literal, TypeVar

_LOGGER: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...
T = TypeVar('T')

class FlowAdapter:
    flow_type: Literal[flow_from, flow_to]
    stat_energy_key: Literal[stat_energy_from, stat_energy_to]
    entity_energy_key: Literal[entity_energy_from, entity_energy_to]
    total_money_key: Literal[stat_cost, stat_compensation]
    name_suffix: str
    entity_id_suffix: str

FLOW_ADAPTERS: Final[Any]

async def _process_manager_data(hass: HomeAssistant, manager: EnergyManager, async_add_entities: AddEntitiesCallback, current_entities: dict[tuple[str, str], EnergyCostSensor]) -> None: ...

class EnergyCostSensor(SensorEntity):
    _adapter: Any
    entity_id: Any
    _attr_device_class: Any
    _attr_state_class: Any
    _flow: Any
    _last_energy_sensor_state: Any
    _cur_value: float
    def __init__(self, adapter: FlowAdapter, flow: dict) -> None: ...
    _attr_state: float
    _attr_last_reset: Any
    def _reset(self, energy_state: State) -> None: ...
    def _update_cost(self) -> None: ...
    _attr_name: Any
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    def update_config(self, flow: dict) -> None: ...
    @property
    def unit_of_measurement(self) -> Union[str, None]: ...
