from .coordinator import RabbitAirConfigEntry as RabbitAirConfigEntry, RabbitAirDataUpdateCoordinator as RabbitAirDataUpdateCoordinator
from .entity import RabbitAirBaseEntity as RabbitAirBaseEntity
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from rabbitair import Quality
from typing import override

def _quality_value(quality: Quality | None) -> StateType: ...

AIR_QUALITY_OPTIONS: Incomplete
AIR_QUALITY_DESCRIPTION: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: RabbitAirConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class RabbitAirAirQualitySensor(RabbitAirBaseEntity, SensorEntity):
    entity_description = AIR_QUALITY_DESCRIPTION
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: RabbitAirDataUpdateCoordinator, entry: RabbitAirConfigEntry) -> None: ...
    @property
    @override
    def native_value(self) -> StateType: ...
