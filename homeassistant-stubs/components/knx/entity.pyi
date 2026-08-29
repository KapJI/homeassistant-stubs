from .const import CONF_DEFAULT_ENTITY_ID as CONF_DEFAULT_ENTITY_ID, DOMAIN as DOMAIN
from .knx_module import KNXModule as KNXModule
from .storage.config_store import PlatformControllerBase as PlatformControllerBase
from .storage.const import CONF_DEVICE_INFO as CONF_DEVICE_INFO
from _typeshed import Incomplete
from dataclasses import dataclass
from homeassistant.const import ATTR_ASSUMED_STATE as ATTR_ASSUMED_STATE, CONF_DEVICE as CONF_DEVICE, CONF_ENTITY_CATEGORY as CONF_ENTITY_CATEGORY, CONF_ID as CONF_ID, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform, async_get_current_platform as async_get_current_platform
from homeassistant.helpers.entity_registry import RegistryEntry as RegistryEntry
from typing import Any, override
from xknx.devices import Device as XknxDevice
from xknx.telegram.address import DeviceGroupAddress as DeviceGroupAddress

_LOGGER: Incomplete

def _stable_group_address_repr(part: DeviceGroupAddress | int | str | None) -> str: ...
def build_yaml_unique_id(*parts: DeviceGroupAddress | int | str | None) -> tuple[str, str]: ...
@callback
def async_migrate_yaml_unique_id(hass: HomeAssistant, platform: str, legacy_id: str, new_id: str) -> None: ...

@dataclass(slots=True, frozen=True)
class KnxEntityIdentifier:
    platform: str
    unique_id: str
    ui: bool

class KnxUiEntityPlatformController(PlatformControllerBase):
    _knx_module: Incomplete
    _entity_platform: Incomplete
    _entity_class: Incomplete
    def __init__(self, knx_module: KNXModule, entity_platform: EntityPlatform, entity_class: type[KnxUiEntity]) -> None: ...
    @override
    async def create_entity(self, unique_id: str, config: dict[str, Any]) -> None: ...
    @override
    async def update_entity(self, entity_entry: RegistryEntry, config: dict[str, Any]) -> None: ...

class _KnxEntityBase(Entity):
    _unrecorded_attributes: Incomplete
    _attr_has_entity_name: bool
    _attr_should_poll: bool
    _attr_unique_id: str
    _knx_module: KNXModule
    _device: XknxDevice
    _knx_entity_identifier: KnxEntityIdentifier | None
    @property
    @override
    def available(self) -> bool: ...
    async def async_update(self) -> None: ...
    def after_update_callback(self, device: XknxDevice) -> None: ...
    @override
    async def async_added_to_hass(self) -> None: ...
    @override
    async def async_will_remove_from_hass(self) -> None: ...

class KnxYamlEntity(_KnxEntityBase):
    _knx_module: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_category: Incomplete
    _attr_device_info: Incomplete
    entity_id: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: tuple[str, str], entity_config: dict[str, Any]) -> None: ...

class KnxUiEntity(_KnxEntityBase):
    _knx_module: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_entity_category: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, knx_module: KNXModule, unique_id: str, entity_config: dict[str, Any]) -> None: ...
