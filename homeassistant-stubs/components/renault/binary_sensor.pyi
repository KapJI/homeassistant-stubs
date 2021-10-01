from .const import DOMAIN as DOMAIN
from .renault_entities import RenaultDataEntity as RenaultDataEntity, RenaultEntityDescription as RenaultEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from homeassistant.components.binary_sensor import BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription, DEVICE_CLASS_BATTERY_CHARGING as DEVICE_CLASS_BATTERY_CHARGING, DEVICE_CLASS_PLUG as DEVICE_CLASS_PLUG
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

class RenaultBinarySensorRequiredKeysMixin:
    on_key: str
    on_value: StateType

class RenaultBinarySensorEntityDescription(BinarySensorEntityDescription, RenaultEntityDescription, RenaultBinarySensorRequiredKeysMixin): ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultBinarySensor(RenaultDataEntity[KamereonVehicleBatteryStatusData], BinarySensorEntity):
    entity_description: RenaultBinarySensorEntityDescription
    @property
    def is_on(self) -> Union[bool, None]: ...

BINARY_SENSOR_TYPES: tuple[RenaultBinarySensorEntityDescription, ...]
