import jinja2
import pathlib
from .storage import async_setup_frontend_storage as async_setup_frontend_storage
from aiohttp import web, web_urldispatcher
from collections.abc import Iterator
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.components.websocket_api.connection import ActiveConnection as ActiveConnection
from homeassistant.config import async_hass_config_yaml as async_hass_config_yaml
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, EVENT_THEMES_UPDATED as EVENT_THEMES_UPDATED
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.translation import async_get_translations as async_get_translations
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from typing import Any, TypedDict
from yarl import URL

DOMAIN: str
CONF_THEMES: str
CONF_THEMES_MODES: str
CONF_THEMES_LIGHT: str
CONF_THEMES_DARK: str
CONF_EXTRA_HTML_URL: str
CONF_EXTRA_HTML_URL_ES5: str
CONF_EXTRA_MODULE_URL: str
CONF_EXTRA_JS_URL_ES5: str
CONF_FRONTEND_REPO: str
CONF_JS_VERSION: str
EVENT_PANELS_UPDATED: str
DEFAULT_THEME_COLOR: str
DATA_PANELS: str
DATA_JS_VERSION: str
DATA_EXTRA_MODULE_URL: str
DATA_EXTRA_JS_URL_ES5: str
THEMES_STORAGE_KEY: Any
THEMES_STORAGE_VERSION: int
THEMES_SAVE_DELAY: int
DATA_THEMES_STORE: str
DATA_THEMES: str
DATA_DEFAULT_THEME: str
DATA_DEFAULT_DARK_THEME: str
DEFAULT_THEME: str
VALUE_NO_THEME: str
PRIMARY_COLOR: str
_LOGGER: Any
EXTENDED_THEME_SCHEMA: Any
THEME_SCHEMA: Any
CONFIG_SCHEMA: Any
SERVICE_SET_THEME: str
SERVICE_RELOAD_THEMES: str

class Manifest:
    manifest: Any
    def __init__(self, data: dict) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    @property
    def json(self) -> str: ...
    _serialized: Any
    def _serialize(self) -> None: ...
    def update_key(self, key: str, val: str) -> None: ...

MANIFEST_JSON: Any

class UrlManager:
    urls: Any
    def __init__(self, urls: list[str]) -> None: ...
    def add(self, url: str) -> None: ...
    def remove(self, url: str) -> None: ...

class Panel:
    component_name: str
    sidebar_icon: Union[str, None]
    sidebar_title: Union[str, None]
    frontend_url_path: Union[str, None]
    config: Union[dict[str, Any], None]
    require_admin: bool
    def __init__(self, component_name: str, sidebar_title: Union[str, None], sidebar_icon: Union[str, None], frontend_url_path: Union[str, None], config: Union[dict[str, Any], None], require_admin: bool) -> None: ...
    def to_response(self) -> PanelRespons: ...

def async_register_built_in_panel(hass: HomeAssistant, component_name: str, sidebar_title: Union[str, None] = ..., sidebar_icon: Union[str, None] = ..., frontend_url_path: Union[str, None] = ..., config: Union[dict[str, Any], None] = ..., require_admin: bool = ..., *, update: bool = ...) -> None: ...
def async_remove_panel(hass: HomeAssistant, frontend_url_path: str) -> None: ...
def add_extra_js_url(hass: HomeAssistant, url: str, es5: bool = ...) -> None: ...
def add_manifest_json_key(key: str, val: Any) -> None: ...
def _frontend_root(dev_repo_path: Union[str, None]) -> pathlib.Path: ...
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def _async_setup_themes(hass: HomeAssistant, themes: Union[dict[str, Any], None]) -> None: ...
def _async_render_index_cached(template: jinja2.Template, **kwargs: Any) -> str: ...

class IndexView(web_urldispatcher.AbstractResource):
    repo_path: Any
    hass: Any
    _template_cache: Any
    def __init__(self, repo_path: Union[str, None], hass: HomeAssistant) -> None: ...
    @property
    def canonical(self) -> str: ...
    @property
    def _route(self) -> web_urldispatcher.ResourceRoute: ...
    def url_for(self, **kwargs: str) -> URL: ...
    async def resolve(self, request: web.Request) -> tuple[Union[web_urldispatcher.UrlMappingMatchInfo, None], set[str]]: ...
    def add_prefix(self, prefix: str) -> None: ...
    def get_info(self) -> dict[str, list[str]]: ...
    def freeze(self) -> None: ...
    def raw_match(self, path: str) -> bool: ...
    def get_template(self) -> jinja2.Template: ...
    async def get(self, request: web.Request) -> web.Response: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[web_urldispatcher.ResourceRoute]: ...

class ManifestJSONView(HomeAssistantView):
    requires_auth: bool
    url: str
    name: str
    def get(self, request: web.Request) -> web.Response: ...

def websocket_get_panels(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
def websocket_get_themes(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def websocket_get_translations(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...
async def websocket_get_version(hass: HomeAssistant, connection: ActiveConnection, msg: dict) -> None: ...

class PanelRespons(TypedDict):
    component_name: str
    icon: Union[str, None]
    title: Union[str, None]
    config: Union[dict[str, Any], None]
    url_path: Union[str, None]
    require_admin: bool
