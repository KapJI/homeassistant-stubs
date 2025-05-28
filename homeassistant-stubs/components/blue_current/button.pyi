from . import BlueCurrentConfigEntry as BlueCurrentConfigEntry, Connector as Connector
from .entity import ChargepointEntity as ChargepointEntity
from _typeshed import Incomplete
from bluecurrent_api.client import Client as Client
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

@dataclass(kw_only=True, frozen=True)
class ChargePointButtonEntityDescription(ButtonEntityDescription):
    function: Callable[[Client, str], Coroutine[Any, Any, None]]

CHARGE_POINT_BUTTONS: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: BlueCurrentConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ChargePointButton(ChargepointEntity, ButtonEntity):
    has_value: bool
    entity_description: ChargePointButtonEntityDescription
    _attr_unique_id: Incomplete
    def __init__(self, connector: Connector, description: ChargePointButtonEntityDescription, evse_id: str) -> None: ...
    async def async_press(self) -> None: ...
