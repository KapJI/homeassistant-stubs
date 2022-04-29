from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.scene import Scene as Scene
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.client import OverkizClient as OverkizClient
from pyoverkiz.models import Scenario as Scenario
from typing import Any

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizScene(Scene):
    scenario: Incomplete
    client: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, scenario: Scenario, client: OverkizClient) -> None: ...
    async def async_activate(self, **kwargs: Any) -> None: ...
