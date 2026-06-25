from . import HuaweiLteConfigEntry as HuaweiLteConfigEntry
from .entity import HuaweiLteBaseEntityWithDevice as HuaweiLteBaseEntityWithDevice
from _typeshed import Incomplete
from homeassistant.components.button import ButtonDeviceClass as ButtonDeviceClass, ButtonEntity as ButtonEntity, ButtonEntityDescription as ButtonEntityDescription
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import entity_platform as entity_platform
from typing import override

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: HuaweiLteConfigEntry, async_add_entities: entity_platform.AddConfigEntryEntitiesCallback) -> None: ...

class BaseButton(HuaweiLteBaseEntityWithDevice, ButtonEntity):
    @property
    @override
    def _device_unique_id(self) -> str: ...
    @override
    async def async_update(self) -> None: ...
    @override
    def press(self) -> None: ...
    def _press(self) -> str: ...

BUTTON_KEY_CLEAR_TRAFFIC_STATISTICS: str

class ClearTrafficStatisticsButton(BaseButton):
    entity_description: Incomplete
    @override
    def _press(self) -> str: ...

BUTTON_KEY_RESTART: str

class RestartButton(BaseButton):
    entity_description: Incomplete
    @override
    def _press(self) -> str: ...
