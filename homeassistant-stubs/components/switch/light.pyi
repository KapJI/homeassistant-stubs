from homeassistant.components import switch as switch
from homeassistant.components.light import LightEntity as LightEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, State as State, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class LightSwitch(LightEntity):
    _name: Any
    _switch_entity_id: Any
    _unique_id: Any
    _switch_state: Any
    def __init__(self, name: str, switch_entity_id: str, unique_id: str) -> None: ...
    @property
    def name(self) -> str: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def available(self) -> bool: ...
    @property
    def should_poll(self) -> bool: ...
    @property
    def unique_id(self): ...
    async def async_turn_on(self, **kwargs) -> None: ...
    async def async_turn_off(self, **kwargs) -> None: ...
    async def async_added_to_hass(self) -> None: ...
