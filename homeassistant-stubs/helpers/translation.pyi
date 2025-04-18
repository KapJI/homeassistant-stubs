import pathlib
from . import singleton as singleton
from _typeshed import Incomplete
from collections.abc import Iterable
from dataclasses import dataclass
from homeassistant.const import EVENT_CORE_CONFIG_UPDATE as EVENT_CORE_CONFIG_UPDATE, STATE_UNAVAILABLE as STATE_UNAVAILABLE, STATE_UNKNOWN as STATE_UNKNOWN
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, async_get_hass as async_get_hass, callback as callback
from homeassistant.loader import Integration as Integration, async_get_config_flows as async_get_config_flows, async_get_integrations as async_get_integrations, bind_hass as bind_hass
from homeassistant.util.json import load_json as load_json
from typing import Any

_LOGGER: Incomplete
TRANSLATION_FLATTEN_CACHE: str
LOCALE_EN: str

def recursive_flatten(prefix: str, data: dict[str, dict[str, Any] | str]) -> dict[str, str]: ...
def _load_translations_files_by_language(translation_files: dict[str, dict[str, pathlib.Path]]) -> dict[str, dict[str, Any]]: ...
def build_resources(translation_strings: dict[str, dict[str, dict[str, Any] | str]], components: set[str], category: str) -> dict[str, dict[str, Any] | str]: ...
async def _async_get_component_strings(hass: HomeAssistant, languages: Iterable[str], components: set[str], integrations: dict[str, Integration]) -> dict[str, dict[str, Any]]: ...

@dataclass(slots=True)
class _TranslationsCacheData:
    loaded: dict[str, set[str]]
    cache: dict[str, dict[str, dict[str, dict[str, str]]]]

class _TranslationCache:
    __slots__: Incomplete
    hass: Incomplete
    cache_data: Incomplete
    lock: Incomplete
    def __init__(self, hass: HomeAssistant) -> None: ...
    @callback
    def async_is_loaded(self, language: str, components: set[str]) -> bool: ...
    async def async_load(self, language: str, components: set[str]) -> None: ...
    async def async_fetch(self, language: str, category: str, components: set[str]) -> dict[str, str]: ...
    def get_cached(self, language: str, category: str, components: set[str]) -> dict[str, str]: ...
    async def _async_load(self, language: str, components: set[str]) -> None: ...
    def _validate_placeholders(self, language: str, updated_resources: dict[str, str], cached_resources: dict[str, str] | None = None) -> dict[str, str]: ...
    @callback
    def _build_category_cache(self, language: str, components: set[str], translation_strings: dict[str, dict[str, Any]]) -> None: ...

@bind_hass
async def async_get_translations(hass: HomeAssistant, language: str, category: str, integrations: Iterable[str] | None = None, config_flow: bool | None = None) -> dict[str, str]: ...
@callback
def async_get_cached_translations(hass: HomeAssistant, language: str, category: str, integration: str | None = None) -> dict[str, str]: ...
def _async_get_translations_cache(hass: HomeAssistant) -> _TranslationCache: ...
@callback
def async_setup(hass: HomeAssistant) -> None: ...
async def async_load_integrations(hass: HomeAssistant, integrations: set[str]) -> None: ...
@callback
def async_translations_loaded(hass: HomeAssistant, components: set[str]) -> bool: ...
@callback
def async_get_exception_message(translation_domain: str, translation_key: str, translation_placeholders: dict[str, str] | None = None) -> str: ...
@callback
def async_translate_state(hass: HomeAssistant, state: str, domain: str, platform: str | None, translation_key: str | None, device_class: str | None) -> str: ...
