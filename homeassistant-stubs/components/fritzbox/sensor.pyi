from . import FritzBoxEntity as FritzBoxEntity
from .const import CONF_COORDINATOR as CONF_COORDINATOR
from .model import FritzEntityDescriptionMixinBase as FritzEntityDescriptionMixinBase
from collections.abc import Callable as Callable
from datetime import datetime
from homeassistant.components.climate.const import PRESET_COMFORT as PRESET_COMFORT, PRESET_ECO as PRESET_ECO
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT as STATE_CLASS_MEASUREMENT, STATE_CLASS_TOTAL_INCREASING as STATE_CLASS_TOTAL_INCREASING, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import DEVICE_CLASS_BATTERY as DEVICE_CLASS_BATTERY, DEVICE_CLASS_ENERGY as DEVICE_CLASS_ENERGY, DEVICE_CLASS_HUMIDITY as DEVICE_CLASS_HUMIDITY, DEVICE_CLASS_POWER as DEVICE_CLASS_POWER, DEVICE_CLASS_TEMPERATURE as DEVICE_CLASS_TEMPERATURE, DEVICE_CLASS_TIMESTAMP as DEVICE_CLASS_TIMESTAMP, ENERGY_KILO_WATT_HOUR as ENERGY_KILO_WATT_HOUR, ENTITY_CATEGORY_DIAGNOSTIC as ENTITY_CATEGORY_DIAGNOSTIC, PERCENTAGE as PERCENTAGE, POWER_WATT as POWER_WATT, TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.util.dt import utc_from_timestamp as utc_from_timestamp
from pyfritzhome.fritzhomedevice import FritzhomeDevice as FritzhomeDevice
from typing import Final

class FritzEntityDescriptionMixinSensor(FritzEntityDescriptionMixinBase):
    native_value: Callable[[FritzhomeDevice], Union[StateType, datetime]]

class FritzSensorEntityDescription(SensorEntityDescription, FritzEntityDescriptionMixinSensor): ...

SENSOR_TYPES: Final[tuple[FritzSensorEntityDescription, ...]]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FritzBoxSensor(FritzBoxEntity, SensorEntity):
    entity_description: FritzSensorEntityDescription
    @property
    def native_value(self) -> Union[StateType, datetime]: ...
