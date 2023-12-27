from .const import CONF_ENTITY_CONFIG as CONF_ENTITY_CONFIG, CONF_EXCLUDE_ACCESSORY_MODE as CONF_EXCLUDE_ACCESSORY_MODE, CONF_FILTER as CONF_FILTER, CONF_HOMEKIT_MODE as CONF_HOMEKIT_MODE, CONF_SUPPORT_AUDIO as CONF_SUPPORT_AUDIO, CONF_VIDEO_CODEC as CONF_VIDEO_CODEC, DEFAULT_CONFIG_FLOW_PORT as DEFAULT_CONFIG_FLOW_PORT, DEFAULT_HOMEKIT_MODE as DEFAULT_HOMEKIT_MODE, DOMAIN as DOMAIN, HOMEKIT_MODES as HOMEKIT_MODES, HOMEKIT_MODE_ACCESSORY as HOMEKIT_MODE_ACCESSORY, HOMEKIT_MODE_BRIDGE as HOMEKIT_MODE_BRIDGE, SHORT_BRIDGE_NAME as SHORT_BRIDGE_NAME, VIDEO_CODEC_COPY as VIDEO_CODEC_COPY
from .util import async_find_next_available_port as async_find_next_available_port, state_needs_accessory_mode as state_needs_accessory_mode
from _typeshed import Incomplete
from collections.abc import Iterable
from homeassistant import config_entries as config_entries
from homeassistant.components import device_automation as device_automation
from homeassistant.config_entries import SOURCE_IMPORT as SOURCE_IMPORT
from homeassistant.const import ATTR_FRIENDLY_NAME as ATTR_FRIENDLY_NAME, CONF_DEVICES as CONF_DEVICES, CONF_DOMAINS as CONF_DOMAINS, CONF_ENTITIES as CONF_ENTITIES, CONF_ENTITY_ID as CONF_ENTITY_ID, CONF_NAME as CONF_NAME, CONF_PORT as CONF_PORT
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback, split_entity_id as split_entity_id
from homeassistant.data_entry_flow import FlowResult as FlowResult
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.entityfilter import CONF_EXCLUDE_DOMAINS as CONF_EXCLUDE_DOMAINS, CONF_EXCLUDE_ENTITIES as CONF_EXCLUDE_ENTITIES, CONF_INCLUDE_DOMAINS as CONF_INCLUDE_DOMAINS, CONF_INCLUDE_ENTITIES as CONF_INCLUDE_ENTITIES
from homeassistant.loader import async_get_integrations as async_get_integrations
from typing import Any

CONF_CAMERA_AUDIO: str
CONF_CAMERA_COPY: str
CONF_INCLUDE_EXCLUDE_MODE: str
MODE_INCLUDE: str
MODE_EXCLUDE: str
INCLUDE_EXCLUDE_MODES: Incomplete
DOMAINS_NEED_ACCESSORY_MODE: Incomplete
NEVER_BRIDGED_DOMAINS: Incomplete
CAMERA_ENTITY_PREFIX: Incomplete
SUPPORTED_DOMAINS: Incomplete
DEFAULT_DOMAINS: Incomplete
_EMPTY_ENTITY_FILTER: dict[str, list[str]]

async def _async_domain_names(hass: HomeAssistant, domains: list[str]) -> str: ...
def _async_build_entites_filter(domains: list[str], entities: list[str]) -> dict[str, Any]: ...
def _async_cameras_from_entities(entities: list[str]) -> dict[str, str]: ...
async def _async_name_to_type_map(hass: HomeAssistant) -> dict[str, str]: ...

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION: int
    hk_data: Incomplete
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_pairing(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def _async_add_entries_for_accessory_mode_entities(self, last_assigned_port: int) -> None: ...
    async def async_step_accessory(self, accessory_input: dict[str, Any]) -> FlowResult: ...
    async def async_step_import(self, user_input: dict[str, Any]) -> FlowResult: ...
    def _async_current_names(self) -> set[str]: ...
    def _async_available_name(self, requested_name: str) -> str: ...
    def _async_is_unique_name_port(self, user_input: dict[str, Any]) -> bool: ...
    @staticmethod
    def async_get_options_flow(config_entry: config_entries.ConfigEntry) -> OptionsFlowHandler: ...

class OptionsFlowHandler(config_entries.OptionsFlow):
    config_entry: Incomplete
    hk_options: Incomplete
    included_cameras: Incomplete
    def __init__(self, config_entry: config_entries.ConfigEntry) -> None: ...
    async def async_step_yaml(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_advanced(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_cameras(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_accessory(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_include(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_exclude(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...
    async def async_step_init(self, user_input: dict[str, Any] | None = None) -> FlowResult: ...

async def _async_get_supported_devices(hass: HomeAssistant) -> dict[str, str]: ...
def _exclude_by_entity_registry(ent_reg: er.EntityRegistry, entity_id: str, include_entity_category: bool, include_hidden: bool) -> bool: ...
def _async_get_matching_entities(hass: HomeAssistant, domains: list[str] | None = None, include_entity_category: bool = False, include_hidden: bool = False) -> dict[str, str]: ...
def _domains_set_from_entities(entity_ids: Iterable[str]) -> set[str]: ...
def _async_get_entity_ids_for_accessory_mode(hass: HomeAssistant, include_domains: Iterable[str]) -> list[str]: ...
def _async_entity_ids_with_accessory_mode(hass: HomeAssistant) -> set[str]: ...
