from .const import DOMAIN as DOMAIN, FORMAT_HTML as FORMAT_HTML, FORMAT_TEXT as FORMAT_TEXT, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from _typeshed import Incomplete
from homeassistant.components.notify import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_TARGET as ATTR_TARGET
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PASSWORD as CONF_PASSWORD, CONF_USERNAME as CONF_USERNAME, CONF_VERIFY_SSL as CONF_VERIFY_SSL, EVENT_HOMEASSISTANT_START as EVENT_HOMEASSISTANT_START, EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.exceptions import ConfigEntryAuthFailed as ConfigEntryAuthFailed, HomeAssistantError as HomeAssistantError
from homeassistant.helpers.json import save_json as save_json
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.json import JsonObjectType as JsonObjectType, load_json_object as load_json_object
from nio import AsyncClient, Event, MatrixRoom as MatrixRoom
from nio.responses import Response as Response
from typing import TypedDict

_LOGGER: Incomplete
SESSION_FILE: str
CONF_HOMESERVER: str
CONF_ROOMS: str
CONF_COMMANDS: str
CONF_WORD: str
CONF_EXPRESSION: str
EVENT_MATRIX_COMMAND: str
DEFAULT_CONTENT_TYPE: str
MESSAGE_FORMATS: Incomplete
DEFAULT_MESSAGE_FORMAT = FORMAT_TEXT
ATTR_FORMAT: str
ATTR_IMAGES: str
WordCommand: Incomplete
ExpressionCommand: Incomplete
RoomID: Incomplete

class ConfigCommand(TypedDict, total=False):
    name: str
    rooms: list[RoomID] | None
    word: WordCommand | None
    expression: ExpressionCommand | None

COMMAND_SCHEMA: Incomplete
CONFIG_SCHEMA: Incomplete
SERVICE_SCHEMA_SEND_MESSAGE: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class MatrixBot:
    _client: AsyncClient
    hass: Incomplete
    _session_filepath: Incomplete
    _access_tokens: Incomplete
    _homeserver: Incomplete
    _verify_tls: Incomplete
    _mx_id: Incomplete
    _password: Incomplete
    _listening_rooms: Incomplete
    _word_commands: Incomplete
    _expression_commands: Incomplete
    def __init__(self, hass: HomeAssistant, config_file: str, homeserver: str, verify_ssl: bool, username: str, password: str, listening_rooms: list[RoomID], commands: list[ConfigCommand]) -> None: ...
    def _load_commands(self, commands: list[ConfigCommand]) -> None: ...
    async def _handle_room_message(self, room: MatrixRoom, message: Event) -> None: ...
    async def _join_room(self, room_id_or_alias: str) -> None: ...
    async def _join_rooms(self) -> None: ...
    async def _get_auth_tokens(self) -> JsonObjectType: ...
    async def _store_auth_token(self, token: str) -> None: ...
    async def _login(self) -> None: ...
    async def _handle_room_send(self, target_room: RoomID, message_type: str, content: dict) -> None: ...
    async def _handle_multi_room_send(self, target_rooms: list[RoomID], message_type: str, content: dict) -> None: ...
    async def _send_image(self, image_path: str, target_rooms: list[RoomID]) -> None: ...
    async def _send_message(self, message: str, target_rooms: list[RoomID], data: dict | None) -> None: ...
    async def handle_send_message(self, service: ServiceCall) -> None: ...
