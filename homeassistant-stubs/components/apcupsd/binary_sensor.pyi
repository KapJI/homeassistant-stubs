from . import APCUPSdData as APCUPSdData, DOMAIN as DOMAIN, VALUE_ONLINE as VALUE_ONLINE
from _typeshed import Incomplete
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_LOGGER: Incomplete
_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OnlineStatus(BinarySensorEntity):
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entity_description: Incomplete
    _data_service: Incomplete
    def __init__(self, data_service: APCUPSdData, description: BinarySensorEntityDescription) -> None: ...
    _attr_available: bool
    _attr_is_on: Incomplete
    def update(self) -> None: ...
