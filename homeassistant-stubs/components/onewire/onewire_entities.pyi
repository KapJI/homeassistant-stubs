from .const import SENSOR_TYPES as SENSOR_TYPES, SENSOR_TYPE_COUNT as SENSOR_TYPE_COUNT, SENSOR_TYPE_SENSED as SENSOR_TYPE_SENSED, SWITCH_TYPE_LATCH as SWITCH_TYPE_LATCH, SWITCH_TYPE_PIO as SWITCH_TYPE_PIO
from .model import DeviceComponentDescription as DeviceComponentDescription
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity
from homeassistant.helpers.typing import StateType as StateType
from pyownet import protocol
from typing import Any

_LOGGER: Any

class OneWireBaseEntity(Entity):
    _name: Any
    _device_file: Any
    _entity_type: Any
    _device_class: Any
    _unit_of_measurement: Any
    _device_info: Any
    _state: Any
    _value_raw: Any
    _default_disabled: Any
    _unique_id: Any
    def __init__(self, name: str, device_file: str, entity_type: str, entity_name: str, device_info: DeviceInfo, default_disabled: bool, unique_id: str) -> None: ...
    @property
    def name(self) -> Union[str, None]: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...
    @property
    def unique_id(self) -> Union[str, None]: ...
    @property
    def device_info(self) -> Union[DeviceInfo, None]: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...

class OneWireProxyEntity(OneWireBaseEntity):
    _owproxy: Any
    def __init__(self, device_id: str, device_name: str, device_info: DeviceInfo, entity_path: str, entity_specs: DeviceComponentDescription, owproxy: protocol._Proxy) -> None: ...
    def _read_value_ownet(self) -> str: ...
    def _write_value_ownet(self, value: bytes) -> None: ...
    _value_raw: Any
    _state: Any
    def update(self) -> None: ...
