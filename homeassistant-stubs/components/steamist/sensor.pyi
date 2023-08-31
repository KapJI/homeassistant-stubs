from .const import DOMAIN as DOMAIN
from .coordinator import SteamistDataUpdateCoordinator as SteamistDataUpdateCoordinator
from .entity import SteamistEntity as SteamistEntity
from _typeshed import Incomplete
from aiosteamist import SteamistStatus as SteamistStatus
from collections.abc import Callable as Callable
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription, SensorStateClass as SensorStateClass
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import UnitOfTemperature as UnitOfTemperature, UnitOfTime as UnitOfTime
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

_KEY_MINUTES_REMAIN: str
_KEY_TEMP: str
UNIT_MAPPINGS: Incomplete

class SteamistSensorEntityDescriptionMixin:
    value_fn: Callable[[SteamistStatus], int | None]
    def __init__(self, value_fn) -> None: ...

class SteamistSensorEntityDescription(SensorEntityDescription, SteamistSensorEntityDescriptionMixin):
    def __init__(self, value_fn, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement, last_reset, native_unit_of_measurement, options, state_class, suggested_display_precision, suggested_unit_of_measurement) -> None: ...

SENSORS: tuple[SteamistSensorEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SteamistSensorEntity(SteamistEntity, SensorEntity):
    entity_description: SteamistSensorEntityDescription
    _attr_native_unit_of_measurement: Incomplete
    def __init__(self, coordinator: SteamistDataUpdateCoordinator, entry: ConfigEntry, description: SteamistSensorEntityDescription) -> None: ...
    @property
    def native_value(self) -> int | None: ...
