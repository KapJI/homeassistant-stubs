import discogs_client
from .const import DEFAULT_NAME as DEFAULT_NAME, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.sensor import SensorEntity as SensorEntity, SensorEntityDescription as SensorEntityDescription
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_TOKEN as CONF_TOKEN
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback, AddEntitiesCallback as AddEntitiesCallback
from homeassistant.helpers.issue_registry import IssueSeverity as IssueSeverity, async_create_issue as async_create_issue
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from typing import Any, override

ATTR_IDENTITY: str
ICON_RECORD: str
ICON_PLAYER: str
UNIT_RECORDS: str
SCAN_INTERVAL: Incomplete
SENSOR_COLLECTION_TYPE: str
SENSOR_WANTLIST_TYPE: str
SENSOR_RANDOM_RECORD_TYPE: str
SENSOR_TYPES: tuple[SensorEntityDescription, ...]
SENSOR_KEYS: list[str]
PLATFORM_SCHEMA: Incomplete

async def async_setup_platform(hass: HomeAssistant, config: ConfigType, async_add_entities: AddEntitiesCallback, discovery_info: DiscoveryInfoType | None = None) -> None: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class DiscogsSensor(SensorEntity):
    _attr_attribution: str
    _attr_has_entity_name: bool
    entity_description: Incomplete
    _client: Incomplete
    _discogs_data: dict[str, Any]
    _attrs: dict[str, Any]
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    def __init__(self, entry: ConfigEntry, client: discogs_client.Client, description: SensorEntityDescription) -> None: ...
    @property
    @override
    def extra_state_attributes(self) -> dict[str, Any] | None: ...
    def get_random_record(self) -> str | None: ...
    _attr_native_value: Incomplete
    def update(self) -> None: ...
