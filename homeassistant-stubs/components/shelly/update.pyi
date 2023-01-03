from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator, get_entry_data as get_entry_data
from .entity import RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import async_remove_shelly_entity as async_remove_shelly_entity, get_block_device_name as get_block_device_name, get_device_entry_gen as get_device_entry_gen, get_rpc_device_name as get_rpc_device_name
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from homeassistant.components.update import UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util import slugify as slugify
from typing import Any, Final

LOGGER: Incomplete

class RpcUpdateRequiredKeysMixin:
    latest_version: Callable[[dict], Any]
    beta: bool
    def __init__(self, latest_version, beta) -> None: ...

class RestUpdateRequiredKeysMixin:
    latest_version: Callable[[dict], Any]
    beta: bool
    def __init__(self, latest_version, beta) -> None: ...

class RpcUpdateDescription(RpcEntityDescription, UpdateEntityDescription, RpcUpdateRequiredKeysMixin):
    def __init__(self, latest_version, beta, sub_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, value, available, removal_condition, extra_state_attributes, use_polling_coordinator, supported) -> None: ...

class RestUpdateDescription(RestEntityDescription, UpdateEntityDescription, RestUpdateRequiredKeysMixin):
    def __init__(self, latest_version, beta, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, value, extra_state_attributes) -> None: ...

REST_UPDATES: Final[Incomplete]
RPC_UPDATES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RestUpdateEntity(ShellyRestAttributeEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    entity_description: RestUpdateDescription
    _in_progress_old_version: Incomplete
    def __init__(self, block_coordinator: ShellyBlockCoordinator, attribute: str, description: RestEntityDescription) -> None: ...
    @property
    def installed_version(self) -> Union[str, None]: ...
    @property
    def latest_version(self) -> Union[str, None]: ...
    @property
    def in_progress(self) -> bool: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...

class RpcUpdateEntity(ShellyRpcAttributeEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    entity_description: RpcUpdateDescription
    _in_progress_old_version: Incomplete
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcEntityDescription) -> None: ...
    @property
    def installed_version(self) -> Union[str, None]: ...
    @property
    def latest_version(self) -> Union[str, None]: ...
    @property
    def in_progress(self) -> bool: ...
    async def async_install(self, version: Union[str, None], backup: bool, **kwargs: Any) -> None: ...
