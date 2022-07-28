from .const import ATTR_DARK as ATTR_DARK, ATTR_ON as ATTR_ON
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.sensor import DOMAIN as DOMAIN, SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE, ATTR_VOLTAGE as ATTR_VOLTAGE, CONCENTRATION_PARTS_PER_BILLION as CONCENTRATION_PARTS_PER_BILLION, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, LIGHT_LUX as LIGHT_LUX, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, PRESSURE_HPA as PRESSURE_HPA, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from pydeconz.interfaces.sensors import SensorResources as SensorResources
from pydeconz.models.event import EventType as EventType

PROVIDES_EXTRA_ATTRIBUTES: Incomplete
ATTR_CURRENT: str
ATTR_POWER: str
ATTR_DAYLIGHT: str
ATTR_EVENT_ID: str

class DeconzSensorDescriptionMixin:
    update_key: str
    value_fn: Callable[[SensorResources], Union[float, int, str, None]]
    def __init__(self, update_key, value_fn) -> None: ...

class DeconzSensorDescription(SensorEntityDescription, DeconzSensorDescriptionMixin):
    suffix: str
    def __init__(self, update_key, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class, suffix) -> None: ...

ENTITY_DESCRIPTIONS: Incomplete
SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzSensor(DeconzDevice, SensorEntity):
    TYPE: Incomplete
    _device: SensorResources
    entity_description: DeconzSensorDescription
    _attr_name: Incomplete
    _update_keys: Incomplete
    def __init__(self, device: SensorResources, gateway: DeconzGateway, description: DeconzSensorDescription) -> None: ...
    @property
    def unique_id(self) -> str: ...
    def async_update_callback(self) -> None: ...
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[bool, float, int, str, None]]: ...

class DeconzBatteryTracker:
    sensor: Incomplete
    gateway: Incomplete
    async_add_entities: Incomplete
    unsub: Incomplete
    def __init__(self, sensor_id: str, gateway: DeconzGateway, async_add_entities: AddEntitiesCallback) -> None: ...
    def async_update_callback(self) -> None: ...
