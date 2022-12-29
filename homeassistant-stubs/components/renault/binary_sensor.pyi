from .const import DOMAIN as DOMAIN
from .renault_entities import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from collections.abc import Callable as Callable
from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass, BinarySensorEntity as BinarySensorEntity, BinarySensorEntityDescription as BinarySensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

class RenaultBinarySensorRequiredKeysMixin:
    on_key: str
    on_value: StateType
    def __init__(self, on_key, on_value) -> None: ...

class RenaultBinarySensorEntityDescription(BinarySensorEntityDescription, RenaultDataEntityDescription, RenaultBinarySensorRequiredKeysMixin):
    icon_fn: Union[Callable[[RenaultBinarySensor], str], None]
    def __init__(self, on_key, on_value, coordinator, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, icon_fn) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultBinarySensor(RenaultDataEntity[KamereonVehicleBatteryStatusData], BinarySensorEntity):
    entity_description: RenaultBinarySensorEntityDescription
    @property
    def is_on(self) -> Union[bool, None]: ...
    @property
    def icon(self) -> Union[str, None]: ...

BINARY_SENSOR_TYPES: tuple[RenaultBinarySensorEntityDescription, ...]
