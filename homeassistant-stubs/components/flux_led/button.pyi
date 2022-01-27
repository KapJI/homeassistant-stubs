from .const import DOMAIN as DOMAIN
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxBaseEntity as FluxBaseEntity
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant import config_entries as config_entries
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_RESTART_KEY: str
_UNPAIR_REMOTES_KEY: str
RESTART_BUTTON_DESCRIPTION: Any
UNPAIR_REMOTES_DESCRIPTION: Any

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxButton(FluxBaseEntity, ButtonEntity):
    _attr_entity_category: Any
    entity_description: Any
    _attr_name: Any
    _attr_unique_id: Any
    def __init__(self, device: AIOWifiLedBulb, entry: config_entries.ConfigEntry, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
