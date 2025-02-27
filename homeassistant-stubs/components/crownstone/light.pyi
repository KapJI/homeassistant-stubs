from .const import CROWNSTONE_INCLUDE_TYPES as CROWNSTONE_INCLUDE_TYPES, CROWNSTONE_SUFFIX as CROWNSTONE_SUFFIX, SIG_CROWNSTONE_STATE_UPDATE as SIG_CROWNSTONE_STATE_UPDATE, SIG_UART_STATE_CHANGE as SIG_UART_STATE_CHANGE
from .entity import CrownstoneEntity as CrownstoneEntity
from .entry_manager import CrownstoneConfigEntry as CrownstoneConfigEntry
from .helpers import map_from_to as map_from_to
from _typeshed import Incomplete
from crownstone_cloud.cloud_models.crownstones import Crownstone as Crownstone
from crownstone_uart import CrownstoneUart as CrownstoneUart
from homeassistant.components.light import ATTR_BRIGHTNESS as ATTR_BRIGHTNESS, ColorMode as ColorMode, LightEntity as LightEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, config_entry: CrownstoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...
def crownstone_state_to_hass(value: int) -> int: ...
def hass_to_crownstone_state(value: int) -> int: ...

class CrownstoneLightEntity(CrownstoneEntity, LightEntity):
    _attr_name: Incomplete
    _attr_translation_key: str
    usb: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, crownstone_data: Crownstone, usb: CrownstoneUart | None = None) -> None: ...
    @property
    def brightness(self) -> int | None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def color_mode(self) -> str: ...
    @property
    def supported_color_modes(self) -> set[str] | None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
