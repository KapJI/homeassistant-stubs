from . import SynoApi as SynoApi
from .const import DOMAIN as DOMAIN
from .coordinator import SynologyDSMSwitchUpdateCoordinator as SynologyDSMSwitchUpdateCoordinator
from .entity import SynologyDSMBaseEntity as SynologyDSMBaseEntity, SynologyDSMEntityDescription as SynologyDSMEntityDescription
from .models import SynologyDSMData as SynologyDSMData
from _typeshed import Incomplete
from homeassistant.components.switch import SwitchEntity as SwitchEntity, SwitchEntityDescription as SwitchEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity import DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback as AddEntitiesCallback
from typing import Any

_LOGGER: Incomplete

class SynologyDSMSwitchEntityDescription(SwitchEntityDescription, SynologyDSMEntityDescription):
    def __init__(self, api_key, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, unit_of_measurement) -> None: ...

SURVEILLANCE_SWITCH: tuple[SynologyDSMSwitchEntityDescription, ...]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None: ...

class SynoDSMSurveillanceHomeModeToggle(SynologyDSMBaseEntity[SynologyDSMSwitchUpdateCoordinator], SwitchEntity):
    entity_description: SynologyDSMSwitchEntityDescription
    _version: Incomplete
    _attr_name: Incomplete
    def __init__(self, api: SynoApi, version: str, coordinator: SynologyDSMSwitchUpdateCoordinator, description: SynologyDSMSwitchEntityDescription) -> None: ...
    @property
    def is_on(self) -> bool: ...
    async def async_turn_on(self, **kwargs: Any) -> None: ...
    async def async_turn_off(self, **kwargs: Any) -> None: ...
    @property
    def available(self) -> bool: ...
    @property
    def device_info(self) -> DeviceInfo: ...
