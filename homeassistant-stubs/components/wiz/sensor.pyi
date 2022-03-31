from .const import DOMAIN as DOMAIN
from .entity import WizEntity as WizEntity
from .models import WizData as WizData
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import SIGNAL_STRENGTH_DECIBELS_MILLIWATT as SIGNAL_STRENGTH_DECIBELS_MILLIWATT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

SENSORS: tuple[SensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class WizSensor(WizEntity, SensorEntity):
    entity_description: SensorEntityDescription
    _attr_unique_id: Any
    _attr_name: Any
    def __init__(self, wiz_data: WizData, name: str, description: SensorEntityDescription) -> None: ...
    _attr_native_value: Any
    def _async_update_attrs(self) -> None: ...
