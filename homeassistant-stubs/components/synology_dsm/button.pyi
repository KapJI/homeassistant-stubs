from . import SynoApi as SynoApi
from .const import DOMAIN as DOMAIN
from .coordinator import SynologyDSMConfigEntry as SynologyDSMConfigEntry
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from typing import Any, Final

LOGGER: Incomplete

@dataclass(frozen=True, kw_only=True)
class SynologyDSMbuttonDescription(ButtonEntityDescription):
    press_action: Callable[[SynoApi], Callable[[], Coroutine[Any, Any, None]]]

BUTTONS: Final[Incomplete]

async def async_setup_entry(hass: HomeAssistant, entry: SynologyDSMConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class SynologyDSMButton(ButtonEntity):
    entity_description: SynologyDSMbuttonDescription
    syno_api: Incomplete
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, api: SynoApi, description: SynologyDSMbuttonDescription) -> None: ...
    async def async_press(self) -> None: ...
