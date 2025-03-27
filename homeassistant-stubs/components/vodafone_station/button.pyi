from .const import DOMAIN as DOMAIN, _LOGGER as _LOGGER
from .coordinator import VodafoneConfigEntry as VodafoneConfigEntry, VodafoneStationRouter as VodafoneStationRouter
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity
from typing import Any, Final

PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class VodafoneStationEntityDescription(ButtonEntityDescription):
    press_action: Callable[[VodafoneStationRouter], Any]
    is_suitable: Callable[[dict], bool]

BUTTON_TYPES: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: VodafoneConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class VodafoneStationSensorEntity(CoordinatorEntity[VodafoneStationRouter], ButtonEntity):
    _attr_has_entity_name: bool
    entity_description: VodafoneStationEntityDescription
    _attr_device_info: Incomplete
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: VodafoneStationRouter, description: VodafoneStationEntityDescription) -> None: ...
    async def async_press(self) -> None: ...
