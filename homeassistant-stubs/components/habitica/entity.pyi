from .const import DOMAIN as DOMAIN, MANUFACTURER as MANUFACTURER, NAME as NAME
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator, HabiticaPartyCoordinator as HabiticaPartyCoordinator
from _typeshed import Incomplete
from habiticalib import ContentData as ContentData, UserData as UserData
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry
from homeassistant.const import CONF_URL as CONF_URL
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.update_coordinator import CoordinatorEntity as CoordinatorEntity

class HabiticaBase(CoordinatorEntity[HabiticaDataUpdateCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    subentry: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator, entity_description: EntityDescription, subentry: ConfigSubentry | None = None) -> None: ...
    @property
    def user(self) -> UserData | None: ...

class HabiticaPartyMemberBase(HabiticaBase):
    party_coordinator: Incomplete
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator, party_coordinator: HabiticaPartyCoordinator, entity_description: EntityDescription, subentry: ConfigSubentry | None = None) -> None: ...
    @property
    def user(self) -> UserData | None: ...
    @property
    def available(self) -> bool: ...
    async def async_added_to_hass(self) -> None: ...

class HabiticaPartyBase(CoordinatorEntity[HabiticaPartyCoordinator]):
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    content: Incomplete
    def __init__(self, coordinator: HabiticaPartyCoordinator, config_entry: HabiticaConfigEntry, entity_description: EntityDescription, content: ContentData) -> None: ...
