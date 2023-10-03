from .deconz_device import DeconzDevice as DeconzDevice
from .gateway import DeconzGateway as DeconzGateway, get_gateway_from_config_entry as get_gateway_from_config_entry
from _typeshed import Incomplete
from homeassistant.components.fan import DOMAIN as DOMAIN, FanEntity as FanEntity, FanEntityFeature as FanEntityFeature
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from homeassistant.util.percentage import ordered_list_item_to_percentage as ordered_list_item_to_percentage, percentage_to_ordered_list_item as percentage_to_ordered_list_item
from pydeconz.models.event import EventType as EventType
from pydeconz.models.light.light import Light, LightFanSpeed
from typing import Any

ORDERED_NAMED_FAN_SPEEDS: list[LightFanSpeed]

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DeconzFan(DeconzDevice[Light], FanEntity):
    TYPE = DOMAIN
    _default_on_speed: Incomplete
    _attr_supported_features: Incomplete
    def __init__(self, device: Light, gateway: DeconzGateway) -> None: ...
    @property
    def is_on(self) -> bool: ...
    @property
    def percentage(self) -> int | None: ...
    def async_update_callback(self) -> None: ...
    async def async_set_percentage(self, percentage: int) -> None: ...
    async def async_turn_on(self, percentage: int | None = ..., preset_mode: str | None = ..., **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
