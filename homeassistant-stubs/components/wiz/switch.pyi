from .const import DOMAIN as DOMAIN
from .entity import WizToggleEntity as WizToggleEntity
from .models import WizData as WizData
from homeassistant.components.switch import SwitchEntity as SwitchEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizSocketEntity(WizToggleEntity, SwitchEntity):
    def __init__(self, wiz_data: WizData, name: str) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
