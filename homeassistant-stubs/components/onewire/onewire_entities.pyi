from .const import READ_MODE_BOOL as READ_MODE_BOOL, READ_MODE_INT as READ_MODE_INT
from _typeshed import Incomplete
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo, Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.typing import StateType as StateType
from pyownet import protocol
from typing import Any

class OneWireEntityDescription(EntityDescription):
    read_mode: Union[str, None]
    def __init__(self, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, name, unit_of_measurement, read_mode) -> None: ...

_LOGGER: Incomplete

class OneWireBaseEntity(Entity):
    entity_description: OneWireEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    _device_file: Incomplete
    _state: Incomplete
    _value_raw: Incomplete
    def __init__(self, description: OneWireEntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, name: str) -> None: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class OneWireProxyEntity(OneWireBaseEntity):
    _owproxy: Incomplete
    def __init__(self, description: OneWireEntityDescription, device_id: str, device_info: DeviceInfo, device_file: str, name: str, owproxy: protocol._Proxy) -> None: ...
    def _read_value_ownet(self) -> str: ...
    def _write_value_ownet(self, value: bytes) -> None: ...
    _value_raw: Incomplete
    _state: Incomplete
    def update(self) -> None: ...
