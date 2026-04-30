from .const import CONF_APP_ID as CONF_APP_ID
from .coordinator import TTNConfigEntry as TTNConfigEntry
from .entity import TTNEntity as TTNEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from ttn_client import TTNSensorValue

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TTNConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TtnDataSensor(TTNEntity, SensorEntity):
    _ttn_value: TTNSensorValue
    @property
    def native_value(self) -> StateType: ...
