from _typeshed import Incomplete
from homeassistant.components import mqtt as mqtt
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.json import json_loads_object as json_loads_object
from typing import Any

_LOGGER: Incomplete
DOMAIN: str
DATA_ARWN: str
TOPIC: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...

class ArwnSensor(SensorEntity):
    _attr_should_poll: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _state_key: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_icon: Incomplete
    _attr_device_class: Incomplete
    _attr_state_class: Incomplete
    _attr_extra_state_attributes: Incomplete
    _attr_native_value: Incomplete
    def __init__(self, unique_id: str, name: str, state_key: str, units: str, icon: str | None = None, device_class: SensorDeviceClass | None = None, state_class: SensorStateClass | None = None, event: dict[str, Any] | None = None) -> None: ...
    def set_event(self, event: dict[str, Any]) -> None: ...
