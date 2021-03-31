from .storage import async_setup_frontend_storage as async_setup_frontend_storage
from aiohttp import web, web_urldispatcher
from homeassistant.components import websocket_api as websocket_api
from homeassistant.components.http.view import HomeAssistantView as HomeAssistantView
from homeassistant.config import async_hass_config_yaml as async_hass_config_yaml
from homeassistant.const import CONF_MODE as CONF_MODE, CONF_NAME as CONF_NAME, EVENT_THEMES_UPDATED as EVENT_THEMES_UPDATED
from homeassistant.core import callback as callback
from homeassistant.helpers import service as service
from homeassistant.helpers.translation import async_get_translations as async_get_translations
from homeassistant.loader import async_get_integration as async_get_integration, bind_hass as bind_hass
from typing import Any, Optional
from yarl import URL

DOMAIN: str
CONF_THEMES: str
CONF_EXTRA_HTML_URL: str
CONF_EXTRA_HTML_URL_ES5: str
CONF_EXTRA_MODULE_URL: str
CONF_EXTRA_JS_URL_ES5: str
CONF_FRONTEND_REPO: str
CONF_JS_VERSION: str
EVENT_PANELS_UPDATED: str
DEFAULT_THEME_COLOR: str
MANIFEST_JSON: Any
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
CONFIG_SCHEMA: Any
SERVICE_SET_THEME: str
SERVICE_RELOAD_THEMES: str

class Panel:
    component_name: Union[str, None] = ...
    sidebar_icon: Union[str, None] = ...
    sidebar_title: Union[str, None] = ...
    frontend_url_path: Union[str, None] = ...
    config: Union[dict[str, Any], None] = ...
    require_admin: bool = ...
    def __init__(self, component_name: Any, sidebar_title: Any, sidebar_icon: Any, frontend_url_path: Any, config: Any, require_admin: Any) -> None: ...
    def to_response(self): ...

def async_register_built_in_panel(hass: Any, component_name: Any, sidebar_title: Optional[Any] = ..., sidebar_icon: Optional[Any] = ..., frontend_url_path: Optional[Any] = ..., config: Optional[Any] = ..., require_admin: bool = ..., *, update: bool = ...) -> None: ...
def async_remove_panel(hass: Any, frontend_url_path: Any) -> None: ...
def add_extra_js_url(hass: Any, url: Any, es5: bool = ...) -> None: ...
def add_manifest_json_key(key: Any, val: Any) -> None: ...
async def async_setup(hass: Any, config: Any): ...

class IndexView(web_urldispatcher.AbstractResource):
    repo_path: Any = ...
    hass: Any = ...
    def __init__(self, repo_path: Any, hass: Any) -> None: ...
    @property
    def canonical(self) -> str: ...
    def url_for(self, **kwargs: str) -> URL: ...
    async def resolve(self, request: web.Request) -> tuple[Union[web_urldispatcher.UrlMappingMatchInfo, None], set[str]]: ...
    def add_prefix(self, prefix: str) -> None: ...
    def get_info(self): ...
    def freeze(self) -> None: ...
    def raw_match(self, path: str) -> bool: ...
    def get_template(self): ...
    async def get(self, request: web.Request) -> web.Response: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Any: ...

class ManifestJSONView(HomeAssistantView):
    requires_auth: bool = ...
    url: str = ...
    name: str = ...
    def get(self, request: Any): ...

def websocket_get_panels(hass: Any, connection: Any, msg: Any) -> None: ...
def websocket_get_themes(hass: Any, connection: Any, msg: Any) -> None: ...
async def websocket_get_translations(hass: Any, connection: Any, msg: Any) -> None: ...
async def websocket_get_version(hass: Any, connection: Any, msg: Any) -> None: ...
