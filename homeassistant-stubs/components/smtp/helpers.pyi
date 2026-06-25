import smtplib
import ssl
from .const import ATTR_HTML as ATTR_HTML, DOMAIN as DOMAIN
from _typeshed import Incomplete
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError

_LOGGER: Incomplete

class SmtpClient:
    _server: Incomplete
    _port: Incomplete
    _timeout: Incomplete
    _sender: Incomplete
    encryption: Incomplete
    username: Incomplete
    password: Incomplete
    _sender_name: Incomplete
    _verify_ssl: Incomplete
    tries: int
    _ssl_context: Incomplete
    def __init__(self, server: str, port: int, timeout: int, sender: str, encryption: str, username: str | None, password: str | None, sender_name: str | None, verify_ssl: bool, ssl_context: ssl.SSLContext | None) -> None: ...
    def connect(self) -> smtplib.SMTP_SSL | smtplib.SMTP: ...
    def connection_is_valid(self) -> bool: ...

def _build_text_msg(message: str) -> MIMEText: ...
def _attach_file(hass: HomeAssistant, atch_name: str, content_id: str | None = None) -> MIMEImage | MIMEApplication | None: ...
def _build_multipart_msg(hass: HomeAssistant, message: str, images: list[str]) -> MIMEMultipart: ...
def _build_html_msg(hass: HomeAssistant, text: str, html: str, images: list[str]) -> MIMEMultipart: ...
