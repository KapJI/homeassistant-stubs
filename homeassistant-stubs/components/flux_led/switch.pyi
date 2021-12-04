from . import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .const import DOMAIN as DOMAIN
from .entity import FluxOnOffEntity as FluxOnOffEntity
from homeassistant import config_entries as config_entries
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxSwitch(FluxOnOffEntity, CoordinatorEntity, SwitchEntity):
    async def _async_turn_on(self, **kwargs: Any) -> None: ...
