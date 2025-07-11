from .const import CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, DOMAIN as DOMAIN
from .helpers import AddressType as AddressType, DeviceConnectionType as DeviceConnectionType, InputType as InputType, LcnConfigEntry as LcnConfigEntry, generate_unique_id as generate_unique_id, get_device_connection as get_device_connection, get_resource as get_resource
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_DOMAIN as CONF_DOMAIN, CONF_NAME as CONF_NAME
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.typing import ConfigType as ConfigType

class LcnEntity(Entity):
    _attr_should_poll: bool
    _attr_has_entity_name: bool
    device_connection: DeviceConnectionType
    config: Incomplete
    config_entry: Incomplete
    address: AddressType
    _unregister_for_inputs: Callable | None
    _name: str
    _attr_device_info: Incomplete
    def __init__(self, config: ConfigType, config_entry: LcnConfigEntry) -> None: ...
    @property
    def unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def name(self) -> str: ...
    def input_received(self, input_obj: InputType) -> None: ...
