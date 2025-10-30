from . import InelsConfigEntry as InelsConfigEntry
from .entity import InelsBaseEntity as InelsBaseEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from inelsmqtt.devices import Device as Device
from inelsmqtt.utils.common import Bit as Bit, Relay as Relay, SimpleRelay as SimpleRelay
from typing import Any

@dataclass(frozen=True, kw_only=True)
class InelsSwitchEntityDescription(SwitchEntityDescription):
    get_state_fn: Callable[[Device, int], Bit | SimpleRelay | Relay]
    alerts: list[str] | None = ...
    placeholder_fn: Callable[[Device, int, bool], dict[str, str]]

SWITCH_TYPES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: InelsConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class InelsSwitch(InelsBaseEntity, SwitchEntity):
    entity_description: InelsSwitchEntityDescription
    _switch_count: Incomplete
    _attr_unique_id: Incomplete
    _attr_translation_placeholders: Incomplete
    def __init__(self, device: Device, description: InelsSwitchEntityDescription, index: int = 0, switch_count: int = 1) -> None: ...
    def _check_alerts(self, current_state: Bit | SimpleRelay | Relay) -> None: ...
    @property
    def is_on(self) -> bool | None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
