from .const import DOMAIN as DOMAIN
from .entity import AnovaDescriptionEntity as AnovaDescriptionEntity
from .models import AnovaData as AnovaData
from homeassistant import config_entries as config_entries
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType

SENSOR_DESCRIPTIONS: list[SensorEntityDescription]

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class AnovaSensor(AnovaDescriptionEntity, SensorEntity):
    @property
    def native_value(self) -> StateType: ...
