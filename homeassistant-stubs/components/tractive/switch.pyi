from . import Trackables as Trackables
from .const import ATTR_BUZZER as ATTR_BUZZER, ATTR_LED as ATTR_LED, ATTR_LIVE_TRACKING as ATTR_LIVE_TRACKING, CLIENT as CLIENT, DOMAIN as DOMAIN, SERVER_UNAVAILABLE as SERVER_UNAVAILABLE, TRACKABLES as TRACKABLES, TRACKER_HARDWARE_STATUS_UPDATED as TRACKER_HARDWARE_STATUS_UPDATED
from .entity import TractiveEntity as TractiveEntity
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ENTITY_CATEGORY_CONFIG as ENTITY_CATEGORY_CONFIG
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any, Literal

_LOGGER: Any

class TractiveRequiredKeysMixin:
    method: Literal[async_set_buzzer, async_set_led, async_set_live_tracking]

class TractiveSwitchEntityDescription(SwitchEntityDescription, TractiveRequiredKeysMixin): ...

SWITCH_TYPES: tuple[TractiveSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TractiveSwitch(TractiveEntity, SwitchEntity):
    entity_description: TractiveSwitchEntityDescription
    _attr_name: Any
    _attr_unique_id: Any
    _attr_available: bool
    _tracker: Any
    _method: Any
    def __init__(self, user_id: str, item: Trackables, description: TractiveSwitchEntityDescription) -> None: ...
    def handle_server_unavailable(self) -> None: ...
    _attr_is_on: Any
    def handle_hardware_status_update(self, event: dict[str, Any]) -> None: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_set_buzzer(self, active: bool) -> dict[str, Any]: ...
    async def async_set_led(self, active: bool) -> dict[str, Any]: ...
    async def async_set_live_tracking(self, active: bool) -> dict[str, Any]: ...
