from .const import ATTRIBUTION as ATTRIBUTION, ATTR_BRAND as ATTR_BRAND, ATTR_CITY as ATTR_CITY, ATTR_FUEL_TYPE as ATTR_FUEL_TYPE, ATTR_HOUSE_NUMBER as ATTR_HOUSE_NUMBER, ATTR_POSTCODE as ATTR_POSTCODE, ATTR_STATION_NAME as ATTR_STATION_NAME, ATTR_STREET as ATTR_STREET
from .coordinator import TankerkoenigConfigEntry as TankerkoenigConfigEntry, TankerkoenigDataUpdateCoordinator as TankerkoenigDataUpdateCoordinator
from .entity import TankerkoenigCoordinatorEntity as TankerkoenigCoordinatorEntity
from _typeshed import Incomplete
from aiotankerkoenig import GasType, Station as Station
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import ATTR_LATITUDE as ATTR_LATITUDE, ATTR_LONGITUDE as ATTR_LONGITUDE, CURRENCY_EURO as CURRENCY_EURO
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int
_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: TankerkoenigConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FuelPriceSensor(TankerkoenigCoordinatorEntity, SensorEntity):
    _attr_attribution = ATTRIBUTION
    _attr_state_class: Incomplete
    _attr_native_unit_of_measurement = CURRENCY_EURO
    _unrecorded_attributes: Incomplete
    _station_id: Incomplete
    _fuel_type: Incomplete
    _attr_translation_key: Incomplete
    _attr_unique_id: Incomplete
    _attr_extra_state_attributes: Incomplete
    def __init__(self, fuel_type: GasType, station: Station, coordinator: TankerkoenigDataUpdateCoordinator) -> None: ...
    @property
    def native_value(self) -> float | None: ...
