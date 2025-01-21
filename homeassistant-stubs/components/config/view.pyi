from .const import ACTION_CREATE_UPDATE as ACTION_CREATE_UPDATE, ACTION_DELETE as ACTION_DELETE
from _typeshed import Incomplete
from aiohttp import web as web
from collections.abc import Callable as Callable, Coroutine
from homeassistant.components.http import HomeAssistantView as HomeAssistantView, KEY_HASS as KEY_HASS, require_admin as require_admin
from homeassistant.const import CONF_ID as CONF_ID
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.exceptions import HomeAssistantError as HomeAssistantError
from homeassistant.util.file import write_utf8_file_atomic as write_utf8_file_atomic
from homeassistant.util.yaml import dump as dump, load_yaml as load_yaml
from homeassistant.util.yaml.loader import JSON_TYPE as JSON_TYPE
from typing import Any

class BaseEditConfigView[_DataT: (dict[str, dict[str, Any]], list[dict[str, Any]])](HomeAssistantView):
    url: Incomplete
    name: Incomplete
    path: Incomplete
    key_schema: Incomplete
    data_schema: Incomplete
    post_write_hook: Incomplete
    data_validator: Incomplete
    mutation_lock: Incomplete
    def __init__(self, component: str, config_type: str, path: str, key_schema: Callable[[Any], str], *, post_write_hook: Callable[[str, str], Coroutine[Any, Any, None]] | None = None, data_schema: Callable[[dict[str, Any]], Any] | None = None, data_validator: Callable[[HomeAssistant, str, dict[str, Any]], Coroutine[Any, Any, dict[str, Any] | None]] | None = None) -> None: ...
    def _empty_config(self) -> _DataT: ...
    def _get_value(self, hass: HomeAssistant, data: _DataT, config_key: str) -> dict[str, Any] | None: ...
    def _write_value(self, hass: HomeAssistant, data: _DataT, config_key: str, new_value: dict[str, Any]) -> None: ...
    def _delete_value(self, hass: HomeAssistant, data: _DataT, config_key: str) -> dict[str, Any] | None: ...
    @require_admin
    async def get(self, request: web.Request, config_key: str) -> web.Response: ...
    @require_admin
    async def post(self, request: web.Request, config_key: str) -> web.Response: ...
    @require_admin
    async def delete(self, request: web.Request, config_key: str) -> web.Response: ...
    async def read_config(self, hass: HomeAssistant) -> _DataT: ...

class EditKeyBasedConfigView(BaseEditConfigView[dict[str, dict[str, Any]]]):
    def _empty_config(self) -> dict[str, Any]: ...
    def _get_value(self, hass: HomeAssistant, data: dict[str, dict[str, Any]], config_key: str) -> dict[str, Any] | None: ...
    def _write_value(self, hass: HomeAssistant, data: dict[str, dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
    def _delete_value(self, hass: HomeAssistant, data: dict[str, dict[str, Any]], config_key: str) -> dict[str, Any]: ...

class EditIdBasedConfigView(BaseEditConfigView[list[dict[str, Any]]]):
    def _empty_config(self) -> list[Any]: ...
    def _get_value(self, hass: HomeAssistant, data: list[dict[str, Any]], config_key: str) -> dict[str, Any] | None: ...
    def _write_value(self, hass: HomeAssistant, data: list[dict[str, Any]], config_key: str, new_value: dict[str, Any]) -> None: ...
    def _delete_value(self, hass: HomeAssistant, data: list[dict[str, Any]], config_key: str) -> None: ...

def _read(path: str) -> JSON_TYPE | None: ...
def _write(path: str, data: dict | list) -> None: ...
