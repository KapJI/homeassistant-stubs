from .const import CONF_GATEWAY_ID as CONF_GATEWAY_ID
from .coordinator import TradfriConfigEntry as TradfriConfigEntry, TradfriDeviceDataUpdateCoordinator as TradfriDeviceDataUpdateCoordinator
from .entity import TradfriBaseEntity as TradfriBaseEntity
from _typeshed import Incomplete
from homeassistant.components.cover import ATTR_POSITION as ATTR_POSITION, CoverEntity as CoverEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from pytradfri.api.aiocoap_api import APIRequestProtocol as APIRequestProtocol
from typing import Any, override

async def async_setup_entry(hass: HomeAssistant, config_entry: TradfriConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class TradfriCover(TradfriBaseEntity, CoverEntity):
    _attr_name: Incomplete
    _device_control: Incomplete
    _device_data: Incomplete
    def __init__(self, device_coordinator: TradfriDeviceDataUpdateCoordinator, api: APIRequestProtocol, gateway_id: str) -> None: ...
    @override
    def _refresh(self) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, str] | None: ...
    @property
    @override
    def current_cover_position(self) -> int | None: ...
    @override
    async def async_set_cover_position(self, **kwargs: Any) -> None: ...
    @override
    async def async_open_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_close_cover(self, **kwargs: Any) -> None: ...
    @override
    async def async_stop_cover(self, **kwargs: Any) -> None: ...
    @property
    @override
    def is_closed(self) -> bool: ...
