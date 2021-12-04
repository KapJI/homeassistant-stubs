from .const import ATTR_SOURCE as ATTR_SOURCE, DATA_KNX_CONFIG as DATA_KNX_CONFIG, DOMAIN as DOMAIN
from .knx_entity import KnxEntity as KnxEntity
from .schema import SensorSchema as SensorSchema
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import CONF_STATE_CLASS as CONF_STATE_CLASS, DEVICE_CLASSES as DEVICE_CLASSES, SensorEntity as SensorEntity
from homeassistant.const import CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_NAME as CONF_NAME, CONF_TYPE as CONF_TYPE, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, StateType as StateType
from typing import Any
from xknx import XKNX as XKNX
from xknx.devices import Sensor as XknxSensor

async def async_setup_entry(hass: HomeAssistant, config_entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...
def _create_sensor(xknx: XKNX, config: ConfigType) -> XknxSensor: ...

class KNXSensor(KnxEntity, SensorEntity):
    _device: XknxSensor
    _attr_device_class: Any
    _attr_force_update: Any
    _attr_entity_category: Any
    _attr_unique_id: Any
    _attr_native_unit_of_measurement: Any
    _attr_state_class: Any
    def __init__(self, xknx: XKNX, config: ConfigType) -> None: ...
    @property
    def native_value(self) -> StateType: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
