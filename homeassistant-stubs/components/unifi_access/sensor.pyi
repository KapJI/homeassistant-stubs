from .coordinator import UnifiAccessConfigEntry as UnifiAccessConfigEntry, UnifiAccessCoordinator as UnifiAccessCoordinator
from .entity import UnifiAccessEntity as UnifiAccessEntity
from _typeshed import Incomplete
from datetime import datetime
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass, SensorEntity as SensorEntity
from homeassistant.const import EntityCategory as EntityCategory
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from unifi_access_api import Door as Door

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: UnifiAccessConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class UnifiAccessDoorLockRuleSensor(UnifiAccessEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_options: Incomplete
    _attr_translation_key: str
    def __init__(self, coordinator: UnifiAccessCoordinator, door: Door) -> None: ...
    @property
    def native_value(self) -> str | None: ...
    @property
    def available(self) -> bool: ...

class UnifiAccessDoorLockRuleEndTimeSensor(UnifiAccessEntity, SensorEntity):
    _attr_device_class: Incomplete
    _attr_entity_category: Incomplete
    _attr_translation_key: str
    def __init__(self, coordinator: UnifiAccessCoordinator, door: Door) -> None: ...
    @property
    def native_value(self) -> datetime | None: ...
    @property
    def available(self) -> bool: ...
