from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import FREQUENCY_GIGAHERTZ as FREQUENCY_GIGAHERTZ
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

ATTR_BRAND: str
ATTR_HZ: str
ATTR_ARCH: str
HZ_ACTUAL: str
HZ_ADVERTISED: str

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class CPUSpeedSensor(SensorEntity):
    _attr_icon: str
    _attr_name: str
    _attr_native_unit_of_measurement: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, entry: ConfigEntry) -> None: ...
    _attr_native_value: Incomplete
    _attr_extra_state_attributes: Incomplete
    def update(self) -> None: ...
