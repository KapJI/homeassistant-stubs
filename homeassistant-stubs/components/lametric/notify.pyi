from .const import CONF_CYCLES as CONF_CYCLES, CONF_ICON_TYPE as CONF_ICON_TYPE, CONF_PRIORITY as CONF_PRIORITY, CONF_SOUND as CONF_SOUND
from .coordinator import LaMetricConfigEntry as LaMetricConfigEntry, LaMetricDataUpdateCoordinator as LaMetricDataUpdateCoordinator
from .entity import LaMetricEntity as LaMetricEntity
from .helpers import lametric_exception_handler as lametric_exception_handler
from _typeshed import Incomplete
from demetriek import LaMetricDevice as LaMetricDevice
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, BaseNotificationService as BaseNotificationService, NotifyEntity as NotifyEntity
from homeassistant.const import CONF_ICON as CONF_ICON
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.enum import try_parse_enum as try_parse_enum
from typing import Any, override

PARALLEL_UPDATES: int

async def async_setup_entry(hass: HomeAssistant, entry: LaMetricConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class LaMetricNotifyEntity(LaMetricEntity, NotifyEntity):
    _attr_translation_key: str
    _attr_unique_id: Incomplete
    def __init__(self, coordinator: LaMetricDataUpdateCoordinator) -> None: ...
    @lametric_exception_handler
    @override
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> LaMetricNotificationService | None: ...

class LaMetricNotificationService(BaseNotificationService):
    lametric: Incomplete
    def __init__(self, lametric: LaMetricDevice) -> None: ...
    @override
    async def async_send_message(self, message: str = '', **kwargs: Any) -> None: ...
