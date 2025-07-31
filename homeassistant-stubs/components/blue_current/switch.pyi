from . import BlueCurrentConfigEntry as BlueCurrentConfigEntry, Connector as Connector, PLUG_AND_CHARGE as PLUG_AND_CHARGE
from .const import AVAILABLE as AVAILABLE, BLOCK as BLOCK, LINKED_CHARGE_CARDS as LINKED_CHARGE_CARDS, PUBLIC_CHARGING as PUBLIC_CHARGING, UNAVAILABLE as UNAVAILABLE, VALUE as VALUE
from .entity import ChargepointEntity as ChargepointEntity
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class BlueCurrentSwitchEntityDescription(SwitchEntityDescription):
    function: Callable[[Connector, str, bool], Any]
    turn_on_off_fn: Callable[[str, Connector], tuple[bool, bool]]

def update_on_value_and_activity(key: str, evse_id: str, connector: Connector, reverse_is_on: bool = False) -> tuple[bool, bool]: ...
def update_block_switch(evse_id: str, connector: Connector) -> tuple[bool, bool]: ...
def update_charge_point(key: str, evse_id: str, connector: Connector, new_switch_value: bool) -> None: ...
async def set_plug_and_charge(connector: Connector, evse_id: str, value: bool) -> None: ...
async def set_linked_charge_cards(connector: Connector, evse_id: str, value: bool) -> None: ...

SWITCHES: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BlueCurrentConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ChargePointSwitch(ChargepointEntity, SwitchEntity):
    has_value: bool
    entity_description: BlueCurrentSwitchEntityDescription
    key: Incomplete
    evse_id: Incomplete
    _attr_available: bool
    _attr_unique_id: Incomplete
    def __init__(self, connector: Connector, evse_id: str, switch: BlueCurrentSwitchEntityDescription) -> None: ...
    async def call_function(self, value: bool) -> None: ...
    _attr_is_on: bool
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @callback
    def update_from_latest_data(self) -> None: ...
