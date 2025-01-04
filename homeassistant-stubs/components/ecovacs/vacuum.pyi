from . import EcovacsConfigEntry as EcovacsConfigEntry
from .const import DOMAIN as DOMAIN
from .entity import EcovacsEntity as EcovacsEntity, EcovacsLegacyEntity as EcovacsLegacyEntity
from .util import get_name_key as get_name_key
from _typeshed import Incomplete
from collections.abc import Mapping
from deebot_client.capabilities import Capabilities
from deebot_client.device import Device as Device
from deebot_client.events import BatteryEvent as BatteryEvent, FanSpeedEvent as FanSpeedEvent, RoomsEvent as RoomsEvent, StateEvent as StateEvent
from deebot_client.models import CleanAction, Room as Room
from homeassistant.components.vacuum import StateVacuumEntity as StateVacuumEntity, StateVacuumEntityDescription as StateVacuumEntityDescription, VacuumActivity as VacuumActivity, VacuumEntityFeature as VacuumEntityFeature
from homeassistant.core import HomeAssistant as HomeAssistant, SupportsResponse as SupportsResponse
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers import entity_platform as entity_platform
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.icon import icon_for_battery_level as icon_for_battery_level
from homeassistant.util import slugify as slugify
from typing import Any

_LOGGER: Incomplete
ATTR_ERROR: str
ATTR_COMPONENT_PREFIX: str
SERVICE_RAW_GET_POSITIONS: str

async def async_setup_entry(hass: HomeAssistant, config_entry: EcovacsConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class EcovacsLegacyVacuum(EcovacsLegacyEntity, StateVacuumEntity):
    _attr_fan_speed_list: Incomplete
    _attr_supported_features: Incomplete
    async def async_added_to_hass(self) -> None: ...
    error: Incomplete
    def on_error(self, error: str) -> None: ...
    @property
    def activity(self) -> VacuumActivity | None: ...
    @property
    def battery_level(self) -> int | None: ...
    @property
    def battery_icon(self) -> str: ...
    @property
    def fan_speed(self) -> str | None: ...
    @property
    def extra_state_attributes(self) -> dict[str, Any]: ...
    def return_to_base(self, **kwargs: Any) -> None: ...
    def start(self, **kwargs: Any) -> None: ...
    def stop(self, **kwargs: Any) -> None: ...
    def clean_spot(self, **kwargs: Any) -> None: ...
    def locate(self, **kwargs: Any) -> None: ...
    def set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    def send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
    async def async_raw_get_positions(self) -> None: ...

_STATE_TO_VACUUM_STATE: Incomplete
_ATTR_ROOMS: str

class EcovacsVacuum(EcovacsEntity[Capabilities], StateVacuumEntity):
    _unrecorded_attributes: Incomplete
    _attr_supported_features: Incomplete
    entity_description: Incomplete
    _rooms: Incomplete
    _attr_fan_speed_list: Incomplete
    def __init__(self, device: Device) -> None: ...
    _attr_battery_level: Incomplete
    _attr_activity: Incomplete
    _attr_fan_speed: Incomplete
    async def async_added_to_hass(self) -> None: ...
    @property
    def extra_state_attributes(self) -> Mapping[str, Any] | None: ...
    async def async_set_fan_speed(self, fan_speed: str, **kwargs: Any) -> None: ...
    async def async_return_to_base(self, **kwargs: Any) -> None: ...
    async def async_stop(self, **kwargs: Any) -> None: ...
    async def async_pause(self) -> None: ...
    async def async_start(self) -> None: ...
    async def _clean_command(self, action: CleanAction) -> None: ...
    async def async_locate(self, **kwargs: Any) -> None: ...
    async def async_send_command(self, command: str, params: dict[str, Any] | list[Any] | None = None, **kwargs: Any) -> None: ...
    async def async_raw_get_positions(self) -> dict[str, Any]: ...
