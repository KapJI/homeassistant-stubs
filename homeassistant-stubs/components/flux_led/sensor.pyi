from .const import DOMAIN as DOMAIN
from .coordinator import FluxLedUpdateCoordinator as FluxLedUpdateCoordinator
from .entity import FluxEntity as FluxEntity
from _typeshed import Incomplete
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class FluxPairedRemotes(FluxEntity, SensorEntity):
    _attr_icon: str
    _attr_entity_category: Incomplete
    @property
    def native_value(self) -> int: ...
