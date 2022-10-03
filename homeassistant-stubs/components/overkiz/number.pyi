from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.number import NumberDeviceClass as NumberDeviceClass, NumberEntity as NumberEntity, NumberEntityDescription as NumberEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import TEMP_CELSIUS as TEMP_CELSIUS
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback

BOOST_MODE_DURATION_DELAY: int
OPERATING_MODE_DELAY: int

class OverkizNumberDescriptionMixin:
    command: str
    def __init__(self, command) -> None: ...

class OverkizNumberDescription(NumberEntityDescription, OverkizNumberDescriptionMixin):
    inverted: bool
    set_native_value: Union[Callable[[float, Callable[..., Awaitable[None]]], Awaitable[None]], None]
    def __init__(self, command, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement, max_value, min_value, native_max_value, native_min_value, native_unit_of_measurement, native_step, step, inverted, set_native_value) -> None: ...

async def _async_set_native_value_boost_mode_duration(value: float, execute_command: Callable[..., Awaitable[None]]) -> None: ...

NUMBER_DESCRIPTIONS: list[OverkizNumberDescription]
SUPPORTED_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizNumber(OverkizDescriptiveEntity, NumberEntity):
    entity_description: OverkizNumberDescription
    @property
    def native_value(self) -> Union[float, None]: ...
    async def async_set_native_value(self, value: float) -> None: ...
