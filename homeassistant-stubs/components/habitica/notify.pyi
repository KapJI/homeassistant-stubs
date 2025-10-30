import abc
from . import HABITICA_KEY as HABITICA_KEY
from .const import DOMAIN as DOMAIN
from .coordinator import HabiticaConfigEntry as HabiticaConfigEntry, HabiticaDataUpdateCoordinator as HabiticaDataUpdateCoordinator
from .entity import HabiticaBase as HabiticaBase
from _typeshed import Incomplete
from abc import abstractmethod
from enum import StrEnum
from habiticalib import GroupData as GroupData, UserData as UserData
from homeassistant.components.notify import NotifyEntity as NotifyEntity, NotifyEntityDescription as NotifyEntityDescription
from homeassistant.const import CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback

PARALLEL_UPDATES: int

class HabiticaNotify(StrEnum):
    PARTY_CHAT = 'party_chat'
    PRIVATE_MESSAGE = 'private_message'

async def async_setup_entry(hass: HomeAssistant, config_entry: HabiticaConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class HabiticaBaseNotifyEntity(HabiticaBase, NotifyEntity, metaclass=abc.ABCMeta):
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator) -> None: ...
    @abstractmethod
    async def _send_message(self, message: str) -> None: ...
    async def async_send_message(self, message: str, title: str | None = None) -> None: ...

class HabiticaPartyChatNotifyEntity(HabiticaBaseNotifyEntity):
    _attr_translation_placeholders: Incomplete
    entity_description: Incomplete
    party: Incomplete
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator, party: GroupData) -> None: ...
    async def _send_message(self, message: str) -> None: ...

class HabiticaPrivateMessageNotifyEntity(HabiticaBaseNotifyEntity):
    _attr_translation_placeholders: Incomplete
    entity_description: Incomplete
    member: Incomplete
    def __init__(self, coordinator: HabiticaDataUpdateCoordinator, member: UserData) -> None: ...
    async def _send_message(self, message: str) -> None: ...
