from .const import DOMAIN as DOMAIN
from .renault_entities import RenaultDataEntity as RenaultDataEntity, RenaultDataEntityDescription as RenaultDataEntityDescription
from .renault_hub import RenaultHub as RenaultHub
from collections.abc import Callable as Callable
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.typing import StateType as StateType
from renault_api.kamereon.models import KamereonVehicleBatteryStatusData

class RenaultSelectRequiredKeysMixin:
    data_key: str
    icon_lambda: Callable[[RenaultSelectEntity], str]
    def __init__(self, data_key, icon_lambda) -> None: ...

class RenaultSelectEntityDescription(SelectEntityDescription, RenaultDataEntityDescription, RenaultSelectRequiredKeysMixin):
    def __init__(self, data_key, icon_lambda, coordinator, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, options) -> None: ...

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class RenaultSelectEntity(RenaultDataEntity[KamereonVehicleBatteryStatusData], SelectEntity):
    entity_description: RenaultSelectEntityDescription
    @property
    def current_option(self) -> Union[str, None]: ...
    @property
    def data(self) -> StateType: ...
    @property
    def icon(self) -> Union[str, None]: ...
    async def async_select_option(self, option: str) -> None: ...

def _get_charge_mode_icon(entity: RenaultSelectEntity) -> str: ...

SENSOR_TYPES: tuple[RenaultSelectEntityDescription, ...]
