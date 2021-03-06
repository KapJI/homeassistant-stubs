from . import LcnEntity as LcnEntity
from .const import CONF_DIMMABLE as CONF_DIMMABLE, CONF_DOMAIN_DATA as CONF_DOMAIN_DATA, CONF_OUTPUT as CONF_OUTPUT, CONF_TRANSITION as CONF_TRANSITION, OUTPUT_PORTS as OUTPUT_PORTS
from .helpers import DeviceConnectionType as DeviceConnectionType, InputType as InputType, get_device_connection as get_device_connection
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ATTR_TRANSITION as ATTR_TRANSITION, LightEntity as LightEntity, SUPPORT_BRIGHTNESS as SUPPORT_BRIGHTNESS, SUPPORT_TRANSITION as SUPPORT_TRANSITION
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ADDRESS as CONF_ADDRESS, CONF_DOMAIN as CONF_DOMAIN, CONF_ENTITIES as CONF_ENTITIES
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

PARALLEL_UPDATES: int

def create_lcn_light_entity(hass: HomeAssistant, entity_config: ConfigType, config_entry: ConfigEntry) -> LcnEntity: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class LcnOutputLight(LcnEntity, LightEntity):
    output: Any
    _transition: Any
    dimmable: Any
    _brightness: int
    _is_on: bool
    _is_dimming_to_zero: bool
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def supported_features(self) -> int: ...
    @property
    def brightness(self) -> Union[int, None]: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def input_received(self, input_obj: InputType) -> None: ...

class LcnRelayLight(LcnEntity, LightEntity):
    output: Any
    _is_on: bool
    def __init__(self, config: ConfigType, entry_id: str, device_connection: DeviceConnectionType) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    def input_received(self, input_obj: InputType) -> None: ...
