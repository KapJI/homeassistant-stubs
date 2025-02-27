from .coordinator import FGLairConfigEntry as FGLairConfigEntry, FGLairCoordinator as FGLairCoordinator
from .entity import FGLairEntity as FGLairEntity
from _typeshed import Incomplete
from ayla_iot_unofficial.fujitsu_hvac import FujitsuHVAC as FujitsuHVAC
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorStateClass as SensorStateClass
from homeassistant.const import UnitOfTemperature as UnitOfTemperature
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

async def async_setup_entry(hass: HomeAssistant, entry: FGLairConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class FGLairOutsideTemperature(FGLairEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_native_unit_of_measurement: Incomplete
    _attr_state_class: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: FGLairCoordinator, device: FujitsuHVAC) -> None: ...
    @property
    def native_value(self) -> float | None: ...
