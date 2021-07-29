from . import RitualsDataUpdateCoordinator as RitualsDataUpdateCoordinator
from .const import COORDINATORS as COORDINATORS, DEVICES as DEVICES, DOMAIN as DOMAIN
from .entity import DiffuserEntity as DiffuserEntity
from homeassistant.components.number import NumberEntity as NumberEntity
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from pyrituals import Diffuser as Diffuser
from typing import Any

MIN_PERFUME_AMOUNT: int
MAX_PERFUME_AMOUNT: int
PERFUME_AMOUNT_SUFFIX: str

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class DiffuserPerfumeAmount(DiffuserEntity, NumberEntity):
    _attr_icon: str
    _attr_max_value: Any
    _attr_min_value: Any
    def __init__(self, diffuser: Diffuser, coordinator: RitualsDataUpdateCoordinator) -> None: ...
    @property
    def value(self) -> int: ...
    async def async_set_value(self, value: float) -> None: ...
