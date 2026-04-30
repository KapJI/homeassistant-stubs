from . import HuaweiLteConfigEntry as HuaweiLteConfigEntry, Router as Router
from .const import KEY_NET_NET_MODE as KEY_NET_NET_MODE
from .entity import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from homeassistant.components.select import SelectEntity as SelectEntity, SelectEntityDescription as SelectEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import Entity as Entity
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any

_LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class HuaweiSelectEntityDescription(SelectEntityDescription):
    setter_fn: Callable[[str], Any]

async def async_setup_entry(hass: HomeAssistant, config_entry: HuaweiLteConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HuaweiLteSelectEntity(HuaweiLteBaseEntityWithDevice, SelectEntity):
    entity_description: HuaweiSelectEntityDescription
    _raw_state: str | None
    key: Incomplete
    item: Incomplete
    def __init__(self, router: Router, entity_description: HuaweiSelectEntityDescription, key: str, item: str) -> None: ...
    def select_option(self, option: str) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    @property
    def _device_unique_id(self) -> str: ...
    async def async_added_to_hass(self) -> None: ...
    async def async_will_remove_from_hass(self) -> None: ...
    _available: bool
    async def async_update(self) -> None: ...
