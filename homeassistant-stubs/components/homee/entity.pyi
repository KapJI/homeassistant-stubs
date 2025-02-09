from . import HomeeConfigEntry as HomeeConfigEntry
from .const import DOMAIN as DOMAIN
from .helpers import get_name_for_enum as get_name_for_enum
from _typeshed import Incomplete
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from pyHomee.const import AttributeType
from pyHomee.model import HomeeAttribute as HomeeAttribute, HomeeNode as HomeeNode

class HomeeEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attribute: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    _attr_device_info: Incomplete
    _host_connected: Incomplete
    def __init__(self, attribute: HomeeAttribute, entry: HomeeConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    def _on_node_updated(self, attribute: HomeeAttribute) -> None: ...
    def _on_connection_changed(self, connected: bool) -> None: ...

class HomeeNodeEntity(Entity):
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _node: Incomplete
    _attr_unique_id: Incomplete
    _entry: Incomplete
    _attr_device_info: Incomplete
    _host_connected: Incomplete
    def __init__(self, node: HomeeNode, entry: HomeeConfigEntry) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    @property
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    def _get_software_version(self) -> str | None: ...
    def has_attribute(self, attribute_type: AttributeType) -> bool: ...
    async def async_set_value(self, attribute: HomeeAttribute, value: float) -> None: ...
    def _on_node_updated(self, node: HomeeNode) -> None: ...
    def _on_connection_changed(self, connected: bool) -> None: ...
