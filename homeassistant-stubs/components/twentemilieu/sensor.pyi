from .const import DOMAIN as DOMAIN, WASTE_TYPE_TO_DESCRIPTION as WASTE_TYPE_TO_DESCRIPTION
from .entity import TwenteMilieuEntity as TwenteMilieuEntity
from datetime import date
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from twentemilieu import WasteType
from typing import Any

class TwenteMilieuSensorDescriptionMixin:
    waste_type: WasteType
    def __init__(self, waste_type) -> None: ...

class TwenteMilieuSensorDescription(SensorEntityDescription, TwenteMilieuSensorDescriptionMixin):
    def __init__(self, waste_type, key, device_class, entity_category, entity_registry_enabled_default, force_update, icon, name, unit_of_measurement, last_reset, native_unit_of_measurement, state_class) -> None: ...

SENSORS: tuple[TwenteMilieuSensorDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class TwenteMilieuSensor(TwenteMilieuEntity, SensorEntity):
    entity_description: TwenteMilieuSensorDescription
    _attr_unique_id: Any
    def __init__(self, coordinator: DataUpdateCoordinator, description: TwenteMilieuSensorDescription, entry: ConfigEntry) -> None: ...
    @property
    def native_value(self) -> Union[date, None]: ...
