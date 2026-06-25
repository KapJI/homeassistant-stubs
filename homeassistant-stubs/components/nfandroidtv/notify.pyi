from . import NFAndroidTVConfigEntry as NFAndroidTVConfigEntry
from .const import ATTR_COLOR as ATTR_COLOR, ATTR_DURATION as ATTR_DURATION, ATTR_FONTSIZE as ATTR_FONTSIZE, ATTR_ICON_AUTH as ATTR_ICON_AUTH, ATTR_ICON_AUTH_DIGEST as ATTR_ICON_AUTH_DIGEST, ATTR_ICON_PASSWORD as ATTR_ICON_PASSWORD, ATTR_ICON_PATH as ATTR_ICON_PATH, ATTR_ICON_URL as ATTR_ICON_URL, ATTR_ICON_USERNAME as ATTR_ICON_USERNAME, ATTR_IMAGE as ATTR_IMAGE, ATTR_IMAGE_AUTH as ATTR_IMAGE_AUTH, ATTR_IMAGE_AUTH_DIGEST as ATTR_IMAGE_AUTH_DIGEST, ATTR_IMAGE_PASSWORD as ATTR_IMAGE_PASSWORD, ATTR_IMAGE_PATH as ATTR_IMAGE_PATH, ATTR_IMAGE_URL as ATTR_IMAGE_URL, ATTR_IMAGE_USERNAME as ATTR_IMAGE_USERNAME, ATTR_INTERRUPT as ATTR_INTERRUPT, ATTR_POSITION as ATTR_POSITION, ATTR_TRANSPARENCY as ATTR_TRANSPARENCY, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.const import ATTR_ICON as ATTR_ICON, CONF_HOST as CONF_HOST, CONF_NAME as CONF_NAME
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError, ServiceValidationError as ServiceValidationError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from io import BufferedReader
from notifications_android_tv.notifications import Notifications
from typing import Any, override

_LOGGER: Incomplete

async def async_setup_entry(hass: HomeAssistant, config_entry: NFAndroidTVConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class NFAndroidTVNotifyEntity(NotifyEntity):
    _attr_supported_features: Incomplete
    _attr_translation_key: str
    _attr_has_entity_name: bool
    _attr_name: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    entry: Incomplete
    client: Incomplete
    def __init__(self, entry: NFAndroidTVConfigEntry) -> None: ...
    @override
    def send_message(self, message: str, title: str | None = None) -> None: ...

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> NFAndroidTVNotificationService | None: ...

class NFAndroidTVNotificationService(BaseNotificationService):
    host: Incomplete
    is_allowed_path: Incomplete
    notify: Notifications | None
    def __init__(self, host: str, is_allowed_path: Any) -> None: ...
    @override
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def load_file(self, url: str | None = None, local_path: str | None = None, username: str | None = None, password: str | None = None, auth: str | None = None) -> BufferedReader | bytes | None: ...
