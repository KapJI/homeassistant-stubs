from homeassistant.components import switch as switch
from homeassistant.components.light import COLOR_MODE_ONOFF as COLOR_MODE_ONOFF, LightEntity as LightEntity, PLATFORM_SCHEMA as PLATFORM_SCHEMA
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, SERVICE_TURN_OFF as SERVICE_TURN_OFF, SERVICE_TURN_ON as SERVICE_TURN_ON, STATE_ON as STATE_ON, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.event import async_track_state_change_event as async_track_state_change_event
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any

DEFAULT_NAME: str

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: Union[DiscoveryInfoType, None] = ...) -> None: ...

class LightSwitch(LightEntity):
    _attr_color_mode: Any
    _attr_should_poll: bool
    _attr_supported_color_modes: Any
    _attr_name: Any
    _attr_unique_id: Any
    _switch_entity_id: Any
    def __init__(self, name: str, switch_entity_id: str, unique_id: Union[str, None]) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    _attr_available: bool
    _attr_is_on: Any
    async def async_added_to_hass(self) -> None: ...
