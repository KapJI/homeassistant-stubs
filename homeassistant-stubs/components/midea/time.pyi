from .const import LOGGER as LOGGER
from .entity import MideaConfigEntry as MideaConfigEntry, MideaDevice as MideaDevice, MideaEntity as MideaEntity, midea_api_call as midea_api_call
from _typeshed import Incomplete
from datetime import time
from homeassistant.components.time import TimeEntity as TimeEntity, TimeEntityDescription as TimeEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import override

PARALLEL_UPDATES: int
TIMES: list[TimeEntityDescription]

async def async_setup_entry(hass: HomeAssistant, config_entry: MideaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MideaTime(MideaEntity, TimeEntity):
    entity_description: TimeEntityDescription
    _hour_attr: Incomplete
    _min_attr: Incomplete
    def __init__(self, device: MideaDevice, entity_description: TimeEntityDescription) -> None: ...
    @property
    @override
    def native_value(self) -> time | None: ...
    @override
    def set_value(self, value: time) -> None: ...
