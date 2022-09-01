from .const import ATTR_DARK as ATTR_DARK, ATTR_ON as ATTR_ON
from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, DOMAIN as DOMAIN
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_TEMPERATURE as ATTR_TEMPERATURE
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pydeconz.interfaces.sensors import SensorResources
from pydeconz.models.event import EventType as EventType
from pydeconz.models.sensor import SensorBase as PydeconzSensorBase
from pydeconz.models.sensor.alarm import Alarm
from pydeconz.models.sensor.carbon_monoxide import CarbonMonoxide
from pydeconz.models.sensor.fire import Fire
from pydeconz.models.sensor.generic_flag import GenericFlag
from pydeconz.models.sensor.open_close import OpenClose
from pydeconz.models.sensor.presence import Presence
from pydeconz.models.sensor.vibration import Vibration
from pydeconz.models.sensor.water import Water
from typing import TypeVar

_SensorDeviceT = TypeVar('_SensorDeviceT', bound=PydeconzSensorBase)
ATTR_ORIENTATION: str
ATTR_TILTANGLE: str
ATTR_VIBRATIONSTRENGTH: str
PROVIDES_EXTRA_ATTRIBUTES: Incomplete

def async_update_unique_id(hass: HomeAssistant, unique_id: str, entity_class: DeconzBinarySensor) -> None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzBinarySensor(DeconzDevice[_SensorDeviceT], BinarySensorEntity):
    old_unique_id_suffix: str
    TYPE: Incomplete
    def __init__(self, device: _SensorDeviceT, gateway: DeconzGateway) -> None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Union[bool, float, int, list, None]]: ...

class DeconzAlarmBinarySensor(DeconzBinarySensor[Alarm]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzCarbonMonoxideBinarySensor(DeconzBinarySensor[CarbonMonoxide]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzFireBinarySensor(DeconzBinarySensor[Fire]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzFireInTestModeBinarySensor(DeconzBinarySensor[Fire]):
    _name_suffix: str
    unique_id_suffix: str
    old_unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzFlagBinarySensor(DeconzBinarySensor[GenericFlag]):
    unique_id_suffix: str
    _update_key: str
    @property
    def is_on(self) -> bool: ...

class DeconzOpenCloseBinarySensor(DeconzBinarySensor[OpenClose]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzPresenceBinarySensor(DeconzBinarySensor[Presence]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzVibrationBinarySensor(DeconzBinarySensor[Vibration]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzWaterBinarySensor(DeconzBinarySensor[Water]):
    unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    @property
    def is_on(self) -> bool: ...

class DeconzTamperedCommonBinarySensor(DeconzBinarySensor[SensorResources]):
    _name_suffix: str
    unique_id_suffix: str
    old_unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    @property
    def is_on(self) -> Union[bool, None]: ...

class DeconzLowBatteryCommonBinarySensor(DeconzBinarySensor[SensorResources]):
    _name_suffix: str
    unique_id_suffix: str
    old_unique_id_suffix: str
    _update_key: str
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    @property
    def is_on(self) -> Union[bool, None]: ...

ENTITY_CLASSES: Incomplete
