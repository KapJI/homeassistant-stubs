from . import NutConfigEntry as NutConfigEntry
from .const import KEY_STATUS as KEY_STATUS, KEY_STATUS_DISPLAY as KEY_STATUS_DISPLAY, STATE_TYPES as STATE_TYPES
from .entity import NUTBaseEntity as NUTBaseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.const import EntityCategory as EntityCategory, PERCENTAGE as PERCENTAGE, UnitOfApparentPower as UnitOfApparentPower, UnitOfElectricCurrent as UnitOfElectricCurrent, UnitOfElectricPotential as UnitOfElectricPotential, UnitOfFrequency as UnitOfFrequency, UnitOfPower as UnitOfPower, UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Final

PARALLEL_UPDATES: int
AMBIENT_PRESENT: str
AMBIENT_SENSORS: Incomplete
BATTERY_CHARGER_STATUS_OPTIONS: Incomplete
FREQUENCY_STATUS_OPTIONS: Incomplete
THRESHOLD_STATUS_OPTIONS: Incomplete
UPS_BEEPER_STATUS_OPTIONS: Incomplete
_LOGGER: Incomplete
SENSOR_TYPES: Final[dict[str, SensorEntityDescription]]

async def async_setup_entry(hass: HomeAssistant, config_entry: NutConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NUTSensor(NUTBaseEntity, SensorEntity):
    @property
    def native_value(self) -> str | None: ...

def _format_display_state(status: dict[str, str]) -> str | None: ...
