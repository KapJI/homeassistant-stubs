from .const import DOMAIN as DOMAIN
from .coordinator import GitHubDataUpdateCoordinator as GitHubDataUpdateCoordinator, GitHubUserDataUpdateCoordinator as GitHubUserDataUpdateCoordinator, GithubConfigEntry as GithubConfigEntry
from _typeshed import Incomplete
from aiogithubapi import GitHubAuthenticatedUserModel as GitHubAuthenticatedUserModel
from collections.abc import Callable as Callable, Mapping
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, override

@dataclass(frozen=True, kw_only=True)
class GitHubSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[dict[str, Any]], StateType]
    attr_fn: Callable[[dict[str, Any]], Mapping[str, Any] | None] = ...
    avabl_fn: Callable[[dict[str, Any]], bool] = ...

SENSOR_DESCRIPTIONS: tuple[GitHubSensorEntityDescription, ...]

@dataclass(frozen=True, kw_only=True)
class GitHubUserSensorEntityDescription(SensorEntityDescription):
    value_fn: Callable[[GitHubAuthenticatedUserModel], StateType]

USER_SENSOR_DESCRIPTIONS: tuple[GitHubUserSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: GithubConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class GitHubSensorEntity(CoordinatorEntity[GitHubDataUpdateCoordinator], SensorEntity):
    _attr_attribution: str
    _attr_has_entity_name: bool
    entity_description: GitHubSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GitHubDataUpdateCoordinator, entity_description: GitHubSensorEntityDescription) -> None: ...
    @property
    @override
    def available(self) -> bool: ...
    @property
    @override
    def native_value(self) -> StateType: ...
    @property
    @override
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...

class GitHubUserSensorEntity(CoordinatorEntity[GitHubUserDataUpdateCoordinator], SensorEntity):
    _attr_has_entity_name: bool
    entity_description: GitHubUserSensorEntityDescription
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: GitHubUserDataUpdateCoordinator, entity_description: GitHubUserSensorEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
