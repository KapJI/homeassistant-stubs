from . import SmtpConfigEntry as SmtpConfigEntry
from .const import ATTR_HTML as ATTR_HTML, ATTR_IMAGES as ATTR_IMAGES, CONF_ENCRYPTION as CONF_ENCRYPTION, CONF_SENDER_NAME as CONF_SENDER_NAME, CONF_SERVER as CONF_SERVER, DEFAULT_DEBUG as DEFAULT_DEBUG, DEFAULT_ENCRYPTION as DEFAULT_ENCRYPTION, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN, ENCRYPTION_OPTIONS as ENCRYPTION_OPTIONS
from .helpers import SmtpClient as SmtpClient, _build_html_msg as _build_html_msg, _build_multipart_msg as _build_multipart_msg, _build_text_msg as _build_text_msg
from .issue import async_deprecate_yaml_issue as async_deprecate_yaml_issue
from _typeshed import Incomplete
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService, NotifyEntity as NotifyEntity, NotifyEntityFeature as NotifyEntityFeature
from homeassistant.config_entries import ConfigSubentry as ConfigSubentry, SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import CONF_DEBUG as CONF_DEBUG, CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RECIPIENT as CONF_RECIPIENT, CONF_SENDER as CONF_SENDER, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.data_entry_flow import FlowResultType as FlowResultType
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.device_registry import DeviceEntryType as DeviceEntryType, DeviceInfo as DeviceInfo
from homeassistant.helpers.entity_platform import AddConfigEntryEntitiesCallback as AddConfigEntryEntitiesCallback
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.ssl import create_client_context as create_client_context
from ssl import SSLContext
from typing import Any, override

PLATFORMS: Incomplete
_LOGGER: Incomplete
PARALLEL_UPDATES: int
PLATFORM_SCHEMA: Incomplete

async def async_get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> MailNotificationService | None: ...
async def async_setup_entry(hass: HomeAssistant, config_entry: SmtpConfigEntry, async_add_entities: AddConfigEntryEntitiesCallback) -> None: ...

class MailNotifyEntity(NotifyEntity):
    _attr_has_entity_name: bool
    _attr_translation_key: str
    _attr_supported_features: Incomplete
    _entry: Incomplete
    _subentry: Incomplete
    _client: Incomplete
    _attr_unique_id: Incomplete
    _attr_device_info: Incomplete
    _attr_name: Incomplete
    def __init__(self, entry: SmtpConfigEntry, subentry: ConfigSubentry, client: SmtpClient) -> None: ...
    @override
    def send_message(self, message: str, title: str | None = None) -> None: ...
    def _send_email(self, msg: MIMEMultipart | MIMEText) -> None: ...

class MailNotificationService(SmtpClient, BaseNotificationService):
    recipients: Incomplete
    def __init__(self, config: DiscoveryInfoType, ssl_context: SSLContext | None) -> None: ...
    @override
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def _send_email(self, msg: MIMEMultipart | MIMEText, recipients: list[str]) -> None: ...
