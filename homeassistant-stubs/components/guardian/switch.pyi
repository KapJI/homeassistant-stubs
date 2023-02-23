from . import GuardianData as GuardianData, ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .const import API_VALVE_STATUS as API_VALVE_STATUS, API_WIFI_STATUS as API_WIFI_STATUS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from aioguardian import Client as Client
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ATTR_AVG_CURRENT: str
ATTR_CONNECTED_CLIENTS: str
ATTR_INST_CURRENT: str
ATTR_INST_CURRENT_DDT: str
ATTR_STATION_CONNECTED: str
ATTR_TRAVEL_COUNT: str
SWITCH_KIND_ONBOARD_AP: str
SWITCH_KIND_VALVE: str

class SwitchDescriptionMixin:
    off_action: Callable[[Client], Awaitable]
    on_action: Callable[[Client], Awaitable]
    def __init__(self, off_action, on_action) -> None: ...

class ValveControllerSwitchDescription(SwitchEntityDescription, ValveControllerEntityDescription, SwitchDescriptionMixin):
    def __init__(self, off_action, on_action, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

async def _async_disable_ap(client: Client) -> None: ...
async def _async_enable_ap(client: Client) -> None: ...
async def _async_close_valve(client: Client) -> None: ...
async def _async_open_valve(client: Client) -> None: ...

VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ValveControllerSwitch(ValveControllerEntity, SwitchEntity):
    ON_STATES: Incomplete
    entity_description: ValveControllerSwitchDescription
    _client: Incomplete
    def __init__(self, entry: ConfigEntry, data: GuardianData, description: ValveControllerSwitchDescription) -> None: ...
    _attr_is_on: Incomplete
    def _async_update_from_latest_data(self) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
