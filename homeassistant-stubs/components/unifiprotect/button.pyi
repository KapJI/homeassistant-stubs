from .const import DEVICES_THAT_ADOPT as DEVICES_THAT_ADOPT, DOMAIN as DOMAIN
from .data import ProtectDeviceType as ProtectDeviceType, UFPConfigEntry as UFPConfigEntry
from .entity import PermRequired as PermRequired, ProtectDeviceEntity as ProtectDeviceEntity, ProtectEntityDescription as ProtectEntityDescription, ProtectSettableKeysMixin as ProtectSettableKeysMixin, T as T, async_all_device_entities as async_all_device_entities
from .utils import async_ufp_instance_command as async_ufp_instance_command
from _typeshed import Incomplete
from collections.abc import Sequence
from dataclasses import dataclass
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.dispatcher import async_dispatcher_connect as async_dispatcher_connect
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from uiprotect.data import ModelType, ProtectAdoptableDeviceModel

_LOGGER: Incomplete
PARALLEL_UPDATES: int

@dataclass(frozen=True, kw_only=True)
class ProtectButtonEntityDescription(ProtectSettableKeysMixin[T], ButtonEntityDescription):
    ufp_press: str | None = ...

ALL_DEVICE_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
ADOPT_BUTTON: Incomplete
SENSOR_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
CHIME_BUTTONS: tuple[ProtectButtonEntityDescription, ...]
_MODEL_DESCRIPTIONS: dict[ModelType, Sequence[ProtectEntityDescription]]

@callback
def _async_remove_adopt_button(hass: HomeAssistant, device: ProtectAdoptableDeviceModel) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: UFPConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ProtectButton(ProtectDeviceEntity, ButtonEntity):
    entity_description: ProtectButtonEntityDescription
    @async_ufp_instance_command
    async def async_press(self) -> None: ...

class ProtectAdoptButton(ProtectButton):
    _attr_available: Incomplete
    @callback
    def _async_update_device_from_protect(self, device: ProtectDeviceType) -> None: ...
