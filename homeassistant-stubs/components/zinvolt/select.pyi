from .coordinator import ZinvoltConfigEntry as ZinvoltConfigEntry, ZinvoltDeviceCoordinator as ZinvoltDeviceCoordinator
from .entity import ZinvoltEntity as ZinvoltEntity
from _typeshed import Incomplete
from homeassistant.components.select import SelectEntity as SelectEntity
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

MODE_MAP: Incomplete
HA_TO_MODE: Incomplete

async def async_setup_entry(hass: HomeAssistant, entry: ZinvoltConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class ZinvoltBatteryMode(ZinvoltEntity, SelectEntity):
    _attr_options: Incomplete
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: ZinvoltDeviceCoordinator) -> None: ...
    @property
    def current_option(self) -> str | None: ...
    async def async_select_option(self, option: str) -> None: ...
