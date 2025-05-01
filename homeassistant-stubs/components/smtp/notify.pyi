import smtplib
import ssl
from .const import ATTR_HTML as ATTR_HTML, ATTR_IMAGES as ATTR_IMAGES, CONF_DEBUG as CONF_DEBUG, CONF_ENCRYPTION as CONF_ENCRYPTION, CONF_SENDER_NAME as CONF_SENDER_NAME, CONF_SERVER as CONF_SERVER, DEFAULT_DEBUG as DEFAULT_DEBUG, DEFAULT_ENCRYPTION as DEFAULT_ENCRYPTION, DEFAULT_HOST as DEFAULT_HOST, DEFAULT_PORT as DEFAULT_PORT, DEFAULT_TIMEOUT as DEFAULT_TIMEOUT, DOMAIN as DOMAIN, ENCRYPTION_OPTIONS as ENCRYPTION_OPTIONS
from _typeshed import Incomplete
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, ATTR_TITLE_DEFAULT as ATTR_TITLE_DEFAULT, BaseNotificationService as BaseNotificationService
from homeassistant.const import CONF_PASSWORD as CONF_PASSWORD, CONF_PORT as CONF_PORT, CONF_RECIPIENT as CONF_RECIPIENT, CONF_SENDER as CONF_SENDER, CONF_TIMEOUT as CONF_TIMEOUT, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.reload import setup_reload_service as setup_reload_service
from homeassistant.helpers.typing import ConfigType as ConfigType, DiscoveryInfoType as DiscoveryInfoType
from homeassistant.util.ssl import create_client_context as create_client_context
from typing import Any

PLATFORMS: Incomplete
_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

def get_service(hass: HomeAssistant, config: ConfigType, discovery_info: DiscoveryInfoType | None = None) -> MailNotificationService | None: ...

class MailNotificationService(BaseNotificationService):
    _server: Incomplete
    _port: Incomplete
    _timeout: Incomplete
    _sender: Incomplete
    encryption: Incomplete
    username: Incomplete
    password: Incomplete
    recipients: Incomplete
    _sender_name: Incomplete
    debug: Incomplete
    _verify_ssl: Incomplete
    tries: int
    _ssl_context: Incomplete
    def __init__(self, server: str, port: int, timeout: int, sender: str, encryption: str, username: str | None, password: str | None, recipients: list[str], sender_name: str | None, debug: bool, verify_ssl: bool, ssl_context: ssl.SSLContext | None) -> None: ...
    def connect(self) -> smtplib.SMTP_SSL | smtplib.SMTP: ...
    def connection_is_valid(self) -> bool: ...
    def send_message(self, message: str, **kwargs: Any) -> None: ...
    def _send_email(self, msg: MIMEMultipart | MIMEText, recipients: list[str]) -> None: ...

def _build_text_msg(message: str) -> MIMEText: ...
def _attach_file(hass: HomeAssistant, atch_name: str, content_id: str | None = None) -> MIMEImage | MIMEApplication | None: ...
def _build_multipart_msg(hass: HomeAssistant, message: str, images: list[str]) -> MIMEMultipart: ...
def _build_html_msg(hass: HomeAssistant, text: str, html: str, images: list[str]) -> MIMEMultipart: ...
