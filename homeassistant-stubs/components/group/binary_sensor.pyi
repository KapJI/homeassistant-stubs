from . import GroupEntity as GroupEntity
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, DEVICE_CLASSES_SCHEMA as DEVICE_CLASSES_SCHEMA, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_DEVICE_CLASS as CONF_DEVICE_CLASS, CONF_ENTITIES as CONF_ENTITIES, CONF_NAME as CONF_NAME, CONF_UNIQUE_ID as CONF_UNIQUE_ID, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import CoreState as CoreState, Event as Event, HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

DEFAULT_NAME: str
CONF_ALL: str
REG_KEY: Any

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[dict[str, Any], None] = ...) -> None: ...

class BinarySensorGroup(GroupEntity, BinarySensorEntity):
    _entity_ids: Any
    _attr_name: Any
    _attr_extra_state_attributes: Any
    _attr_unique_id: Any
    _device_class: Any
    _state: Any
    mode: Any
    def __init__(self, unique_id: Union[str, None], name: str, device_class: Union[str, None], entity_ids: list[str], mode: Union[str, None]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    _attr_available: Any
    _attr_is_on: Any
    async def async_update(self) -> None: ...
    @property
    def device_class(self) -> Union[str, None]: ...
