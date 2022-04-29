from .entity import WemoEntity as WemoEntity
from .wemo_device import DeviceCoordinator as DeviceCoordinator
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, POWER_WATT as POWER_WATT
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

class AttributeSensorDescription(SensorEntityDescription):
    state_conversion: Union[Callable[[StateType], StateType], None]
    unique_id_suffix: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, state_conversion, unique_id_suffix) -> None: ...

ATTRIBUTE_SENSORS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AttributeSensor(WemoEntity, SensorEntity):
    entity_description: AttributeSensorDescription
    def __init__(self, coordinator: DeviceCoordinator, description: AttributeSensorDescription) -> None: ...
    @property
    def name_suffix(self) -> Union[str, None]: ...
    @property
    def unique_id_suffix(self) -> Union[str, None]: ...
    def convert_state(self, value: StateType) -> StateType: ...
    @property
    def native_value(self) -> StateType: ...
