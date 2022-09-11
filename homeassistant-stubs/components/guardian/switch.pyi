from . import GuardianData as GuardianData, ValveControllerEntity as ValveControllerEntity, ValveControllerEntityDescription as ValveControllerEntityDescription
from .const import API_VALVE_STATUS as API_VALVE_STATUS, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

ATTR_AVG_CURRENT: str
ATTR_INST_CURRENT: str
ATTR_INST_CURRENT_DDT: str
ATTR_TRAVEL_COUNT: str
SWITCH_KIND_VALVE: str

class ValveControllerSwitchDescription(SwitchEntityDescription, ValveControllerEntityDescription):
    def __init__(self, api_category, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

VALVE_CONTROLLER_DESCRIPTIONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class ValveControllerSwitch(ValveControllerEntity, SwitchEntity):
    entity_description: ValveControllerSwitchDescription
    ON_STATES: Incomplete
    _attr_is_on: bool
    _client: Incomplete
    def __init__(self, entry: ConfigEntry, data: GuardianData, description: ValveControllerSwitchDescription) -> None: ...
    def _async_update_from_latest_data(self) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
