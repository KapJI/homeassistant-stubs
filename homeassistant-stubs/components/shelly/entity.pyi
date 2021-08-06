import aioshelly
from . import ShellyDeviceRestWrapper as ShellyDeviceRestWrapper, ShellyDeviceWrapper as ShellyDeviceWrapper
from .const import AIOSHELLY_DEVICE_TIMEOUT_SEC as AIOSHELLY_DEVICE_TIMEOUT_SEC, COAP as COAP, DATA_CONFIG_ENTRY as DATA_CONFIG_ENTRY, DOMAIN as DOMAIN, REST as REST
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_entity_name as get_entity_name
from homeassistant.components.sensor import ATTR_STATE_CLASS as ATTR_STATE_CLASS
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import device_registry as device_registry, entity as entity, entity_registry as entity_registry, update_coordinator as update_coordinator
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.typing import StateType as StateType
from typing import Any, Callable, Final

_LOGGER: Final[Any]

async def async_setup_entry_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: dict[tuple[str, str], BlockAttributeDescription], sensor_class: Callable) -> None: ...
async def async_setup_block_attribute_entities(hass: HomeAssistant, async_add_entities: AddEntitiesCallback, wrapper: ShellyDeviceWrapper, sensors: dict[tuple[str, str], BlockAttributeDescription], sensor_class: Callable) -> None: ...
async def async_restore_block_attribute_entities(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, wrapper: ShellyDeviceWrapper, sensors: dict[tuple[str, str], BlockAttributeDescription], sensor_class: Callable) -> None: ...
async def async_setup_entry_rest(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback, sensors: dict[str, RestAttributeDescription], sensor_class: Callable) -> None: ...

class BlockAttributeDescription:
    name: str
    icon: Union[str, None]
    unit: Union[None, str, Callable[[dict], str]]
    value: Callable[[Any], Any]
    device_class: Union[str, None]
    state_class: Union[str, None]
    default_enabled: bool
    available: Union[Callable[[aioshelly.Block], bool], None]
    removal_condition: Union[Callable[[dict, aioshelly.Block], bool], None]
    extra_state_attributes: Union[Callable[[aioshelly.Block], Union[dict, None]], None]
    last_reset: Union[str, None]

class RestAttributeDescription:
    name: str
    icon: Union[str, None]
    unit: Union[str, None]
    value: Union[Callable[[dict, Any], Any], None]
    device_class: Union[str, None]
    state_class: Union[str, None]
    default_enabled: bool
    extra_state_attributes: Union[Callable[[dict], Union[dict, None]], None]

class ShellyBlockEntity(entity.Entity):
    wrapper: Any
    block: Any
    _name: Any
    def __init__(self, wrapper: ShellyDeviceWrapper, block: aioshelly.Block) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def available(self) -> bool: ...
    @property
    def unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_update(self) -> None: ...
    def _update_callback(self) -> None: ...
    async def set_state(self, **kwargs: Any) -> Any: ...

class ShellyBlockAttributeEntity(ShellyBlockEntity, entity.Entity):
    attribute: Any
    description: Any
    _unit: Any
    _unique_id: Any
    _name: Any
    def __init__(self, wrapper: ShellyDeviceWrapper, block: aioshelly.Block, attribute: str, description: BlockAttributeDescription) -> None: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def available(self) -> bool: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class ShellyRestAttributeEntity(update_coordinator.CoordinatorEntity):
    wrapper: Any
    attribute: Any
    description: Any
    _name: Any
    _last_value: Any
    def __init__(self, wrapper: ShellyDeviceWrapper, attribute: str, description: RestAttributeDescription) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def device_info(self) -> DeviceInfo: ...
    @property
    def entity_registry_enabled_default(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def attribute_value(self) -> StateType: ...
    @property
    def device_class(self) -> Union[str, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...
    @property
    def unique_id(self) -> str: ...
    @property
    def extra_state_attributes(self) -> Union[dict[str, Any], None]: ...

class ShellySleepingBlockAttributeEntity(ShellyBlockAttributeEntity, RestoreEntity):
    sensors: Any
    last_state: Any
    wrapper: Any
    attribute: Any
    block: Any
    description: Any
    _unit: Any
    _unique_id: Any
    _name: Any
    def __init__(self, wrapper: ShellyDeviceWrapper, block: aioshelly.Block, attribute: str, description: BlockAttributeDescription, entry: Union[entity_registry.RegistryEntry, None] = ..., sensors: Union[dict[tuple[str, str], BlockAttributeDescription], None] = ...) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    def _update_callback(self) -> None: ...
