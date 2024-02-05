from .api import MinecraftServerData as MinecraftServerData, MinecraftServerType as MinecraftServerType
from .const import DOMAIN as DOMAIN, KEY_LATENCY as KEY_LATENCY, KEY_MOTD as KEY_MOTD
from .coordinator import MinecraftServerCoordinator as MinecraftServerCoordinator
from .entity import MinecraftServerEntity as MinecraftServerEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable, MutableMapping
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TYPE as CONF_TYPE, EntityCategory as EntityCategory, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from typing import Any

ATTR_PLAYERS_LIST: str
ICON_EDITION: str
ICON_GAME_MODE: str
ICON_MAP_NAME: str
ICON_LATENCY: str
ICON_PLAYERS_MAX: str
ICON_PLAYERS_ONLINE: str
ICON_PROTOCOL_VERSION: str
ICON_VERSION: str
ICON_MOTD: str
KEY_EDITION: str
KEY_GAME_MODE: str
KEY_MAP_NAME: str
KEY_PLAYERS_MAX: str
KEY_PLAYERS_ONLINE: str
KEY_PROTOCOL_VERSION: str
KEY_VERSION: str
UNIT_PLAYERS_MAX: str
UNIT_PLAYERS_ONLINE: str

@dataclass(frozen=True)
class MinecraftServerEntityDescriptionMixin:
    value_fn: Callable[[MinecraftServerData], StateType]
    attributes_fn: Callable[[MinecraftServerData], MutableMapping[str, Any]] | None
    supported_server_types: set[MinecraftServerType]
    def __init__(self, value_fn, attributes_fn, supported_server_types) -> None: ...

@dataclass(frozen=True)
class MinecraftServerSensorEntityDescription(SensorEntityDescription, MinecraftServerEntityDescriptionMixin):
    def __init__(self, value_fn, attributes_fn, supported_server_types, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

def get_extra_state_attributes_players_list(data: MinecraftServerData) -> dict[str, list[str]]: ...

SENSOR_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class MinecraftServerSensorEntity(MinecraftServerEntity, SensorEntity):
    entity_description: MinecraftServerSensorEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: MinecraftServerCoordinator, description: MinecraftServerSensorEntityDescription, config_entry: ConfigEntry) -> None: ...
    def _handle_coordinator_update(self) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def _update_properties(self) -> None: ...
