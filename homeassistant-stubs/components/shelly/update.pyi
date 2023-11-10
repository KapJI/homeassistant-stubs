from .const import CONF_SLEEP_PERIOD as CONF_SLEEP_PERIOD, OTA_BEGIN as OTA_BEGIN, OTA_ERROR as OTA_ERROR, OTA_PROGRESS as OTA_PROGRESS, OTA_SUCCESS as OTA_SUCCESS
from .coordinator import ShellyBlockCoordinator as ShellyBlockCoordinator, ShellyRpcCoordinator as ShellyRpcCoordinator
from .entity import RestEntityDescription as RestEntityDescription, RpcEntityDescription as RpcEntityDescription, ShellyRestAttributeEntity as ShellyRestAttributeEntity, ShellyRpcAttributeEntity as ShellyRpcAttributeEntity, ShellySleepingRpcAttributeEntity as ShellySleepingRpcAttributeEntity, async_setup_entry_rest as async_setup_entry_rest, async_setup_entry_rpc as async_setup_entry_rpc
from .utils import get_device_entry_gen as get_device_entry_gen
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.update import ATTR_INSTALLED_VERSION as ATTR_INSTALLED_VERSION, ATTR_LATEST_VERSION as ATTR_LATEST_VERSION, UpdateDeviceClass as UpdateDeviceClass, UpdateEntity as UpdateEntity, UpdateEntityDescription as UpdateEntityDescription, UpdateEntityFeature as UpdateEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from typing import Any, Final

LOGGER: Incomplete

@dataclass
class RpcUpdateRequiredKeysMixin:
    latest_version: Callable[[dict], Any]
    beta: bool
    def __init__(self, latest_version, beta) -> None: ...

@dataclass
class RestUpdateRequiredKeysMixin:
    latest_version: Callable[[dict], Any]
    beta: bool
    def __init__(self, latest_version, beta) -> None: ...

@dataclass
class RpcUpdateDescription(RpcEntityDescription, UpdateEntityDescription, RpcUpdateRequiredKeysMixin):
    def __init__(self, latest_version, beta, sub_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, value, available, removal_condition, extra_state_attributes, use_polling_coordinator, supported) -> None: ...

@dataclass
class RestUpdateDescription(RestEntityDescription, UpdateEntityDescription, RestUpdateRequiredKeysMixin):
    def __init__(self, latest_version, beta, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, value, extra_state_attributes) -> None: ...

REST_UPDATES: Final[Incomplete]
RPC_UPDATES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RestUpdateEntity(ShellyRestAttributeEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    entity_description: RestUpdateDescription
    _in_progress_old_version: Incomplete
    def __init__(self, block_coordinator: ShellyBlockCoordinator, attribute: str, description: RestEntityDescription) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    @property
    def in_progress(self) -> bool: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...

class RpcUpdateEntity(ShellyRpcAttributeEntity, UpdateEntity):
    _attr_supported_features: Incomplete
    entity_description: RpcUpdateDescription
    _ota_in_progress: bool
    def __init__(self, coordinator: ShellyRpcCoordinator, key: str, attribute: str, description: RpcEntityDescription) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_in_progress: int
    def _ota_progress_callback(self, event: dict[str, Any]) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
    async def async_install(self, version: str | None, backup: bool, **kwargs: Any) -> None: ...

class RpcSleepingUpdateEntity(ShellySleepingRpcAttributeEntity, UpdateEntity, RestoreEntity):
    entity_description: RpcUpdateDescription
    last_state: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def installed_version(self) -> str | None: ...
    @property
    def latest_version(self) -> str | None: ...
