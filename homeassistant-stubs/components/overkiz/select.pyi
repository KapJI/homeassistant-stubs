from . import HomeAssistantOverkizData as HomeAssistantOverkizData
from .const import DOMAIN as DOMAIN, IGNORED_OVERKIZ_DEVICES as IGNORED_OVERKIZ_DEVICES
from .entity import OverkizDescriptiveEntity as OverkizDescriptiveEntity, OverkizDeviceClass as OverkizDeviceClass
from _typeshed import Incomplete
from collections.abc import Awaitable, Callable as Callable
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import EntityCategory as EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyoverkiz.enums import OverkizCommandParam

class OverkizSelectDescriptionMixin:
    options: list[Union[str, OverkizCommandParam]]
    select_option: Callable[[str, Callable[..., Awaitable[None]]], Awaitable[None]]
    def __init__(self, options, select_option) -> None: ...

class OverkizSelectDescription(SelectEntityDescription, OverkizSelectDescriptionMixin):
    def __init__(self, options, select_option, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, unit_of_measurement) -> None: ...

def _select_option_open_closed_pedestrian(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...
def _select_option_memorized_simple_volume(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...
def _select_option_active_zone(option: str, execute_command: Callable[..., Awaitable[None]]) -> Awaitable[None]: ...

SELECT_DESCRIPTIONS: list[OverkizSelectDescription]
SUPPORTED_STATES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class OverkizSelect(OverkizDescriptiveEntity, SelectEntity):
    entity_description: OverkizSelectDescription
    @property
    def current_option(self) -> Union[str, None]: ...
    @property
    def options(self) -> list[str]: ...
    async def async_select_option(self, option: str) -> None: ...
