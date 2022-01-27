from . import VelbusEntity as VelbusEntity
from .const import DOMAIN as DOMAIN
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any
from velbusaio.channels import ButtonCounter as ButtonCounter, LightSensor as LightSensor, SensorNumber as SensorNumber, Temperature as Temperature

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class VelbusSensor(VelbusEntity, SensorEntity):
    _channel: Union[ButtonCounter, Temperature, LightSensor, SensorNumber]
    _is_counter: Any
    _attr_unique_id: Any
    _attr_name: Any
    _attr_device_class: Any
    _attr_icon: str
    _attr_state_class: Any
    _attr_native_unit_of_measurement: Any
    def __init__(self, channel: Union[ButtonCounter, Temperature, LightSensor, SensorNumber], counter: bool = ...) -> None: ...
    @property
    def native_value(self) -> Union[float, int, None]: ...
