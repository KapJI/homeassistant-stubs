from .coordinator import FluxLedConfigEntry as FluxLedConfigEntry
from .entity import FluxBaseEntity as FluxBaseEntity
from _typeshed import Incomplete
from flux_led.aio import AIOWifiLedBulb as AIOWifiLedBulb
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

_RESTART_KEY: str
_UNPAIR_REMOTES_KEY: str
RESTART_BUTTON_DESCRIPTION: Incomplete
UNPAIR_REMOTES_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: FluxLedConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FluxButton(FluxBaseEntity, ButtonEntity):
    _attr_entity_category: Incomplete
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, device: AIOWifiLedBulb, entry: FluxLedConfigEntry, description: ButtonEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
