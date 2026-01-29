from .const import DOMAIN as DOMAIN
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationRouter as VodafoneStationRouter
from _typeshed import Incomplete
from aiovodafone.const import WifiBand, WifiType
from dataclasses import dataclass
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VodafoneStationEntityDescription(SwitchEntityDescription):
    band: WifiBand
    typology: WifiType

SWITCHES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VodafoneSwitchEntity(CoordinatorEntity[VodafoneStationRouter], SwitchEntity):
    _attr_has_entity_name: bool
    entity_description: VodafoneStationEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VodafoneStationRouter, description: VodafoneStationEntityDescription) -> None: ...
    async def _set_wifi_status(self, status: bool) -> None: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def is_on(self) -> bool: ...
