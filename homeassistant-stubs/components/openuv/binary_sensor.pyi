from .const import DATA_PROTECTION_WINDOW as DATA_PROTECTION_WINDOW, DOMAIN as DOMAIN, LOGGER as LOGGER, TYPE_PROTECTION_WINDOW as TYPE_PROTECTION_WINDOW
from .coordinator import OpenUvCoordinator as OpenUvCoordinator
from .entity import OpenUvEntity as OpenUvEntity
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.util.dt import as_local as as_local, parse_datetime as parse_datetime, utcnow as utcnow

ATTR_PROTECTION_WINDOW_ENDING_TIME: str
ATTR_PROTECTION_WINDOW_ENDING_UV: str
ATTR_PROTECTION_WINDOW_STARTING_TIME: str
ATTR_PROTECTION_WINDOW_STARTING_UV: str
BINARY_SENSOR_DESCRIPTION_PROTECTION_WINDOW: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class OpenUvBinarySensor(OpenUvEntity, BinarySensorEntity):
    @callback
    def _handle_coordinator_update(self) -> None: ...
    _attr_is_on: bool
    def _update_attrs(self) -> None: ...
