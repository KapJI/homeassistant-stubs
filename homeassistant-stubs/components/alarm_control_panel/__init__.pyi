import asyncio
from .const import ATTR_CHANGED_BY as ATTR_CHANGED_BY, ATTR_CODE_ARM_REQUIRED as ATTR_CODE_ARM_REQUIRED, AlarmControlPanelEntityFeature as AlarmControlPanelEntityFeature, AlarmControlPanelState as AlarmControlPanelState, CodeFormat as CodeFormat, DOMAIN as DOMAIN, _DEPRECATED_FORMAT_NUMBER as _DEPRECATED_FORMAT_NUMBER, _DEPRECATED_FORMAT_TEXT as _DEPRECATED_FORMAT_TEXT, _DEPRECATED_SUPPORT_ALARM_ARM_AWAY as _DEPRECATED_SUPPORT_ALARM_ARM_AWAY, _DEPRECATED_SUPPORT_ALARM_ARM_CUSTOM_BYPASS as _DEPRECATED_SUPPORT_ALARM_ARM_CUSTOM_BYPASS, _DEPRECATED_SUPPORT_ALARM_ARM_HOME as _DEPRECATED_SUPPORT_ALARM_ARM_HOME, _DEPRECATED_SUPPORT_ALARM_ARM_NIGHT as _DEPRECATED_SUPPORT_ALARM_ARM_NIGHT, _DEPRECATED_SUPPORT_ALARM_ARM_VACATION as _DEPRECATED_SUPPORT_ALARM_ARM_VACATION, _DEPRECATED_SUPPORT_ALARM_TRIGGER as _DEPRECATED_SUPPORT_ALARM_TRIGGER
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import ATTR_CODE as ATTR_CODE, ATTR_CODE_FORMAT as ATTR_CODE_FORMAT, SERVICE_ALARM_ARM_AWAY as SERVICE_ALARM_ARM_AWAY, SERVICE_ALARM_ARM_CUSTOM_BYPASS as SERVICE_ALARM_ARM_CUSTOM_BYPASS, SERVICE_ALARM_ARM_HOME as SERVICE_ALARM_ARM_HOME, SERVICE_ALARM_ARM_NIGHT as SERVICE_ALARM_ARM_NIGHT, SERVICE_ALARM_ARM_VACATION as SERVICE_ALARM_ARM_VACATION, SERVICE_ALARM_DISARM as SERVICE_ALARM_DISARM, SERVICE_ALARM_TRIGGER as SERVICE_ALARM_TRIGGER
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.exceptions import ServiceValidationError as ServiceValidationError
from homeassistant.helpers.config_validation import make_entity_service_schema as make_entity_service_schema
from homeassistant.helpers.deprecation import all_with_deprecated_constants as all_with_deprecated_constants, check_if_deprecated_constant as check_if_deprecated_constant, dir_with_deprecated_constants as dir_with_deprecated_constants
from homeassistant.helpers.entity import Entity as Entity, EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.entity_platform import EntityPlatform as EntityPlatform
from homeassistant.helpers.frame import ReportBehavior as ReportBehavior, report_usage as report_usage
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Final

_LOGGER: Final[Incomplete]
DATA_COMPONENT: HassKey[EntityComponent[AlarmControlPanelEntity]]
ENTITY_ID_FORMAT: Final[Incomplete]
PLATFORM_SCHEMA: Final[Incomplete]
PLATFORM_SCHEMA_BASE: Final[Incomplete]
SCAN_INTERVAL: Final[Incomplete]
CONF_DEFAULT_CODE: str
ALARM_SERVICE_SCHEMA: Final[Incomplete]

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class AlarmControlPanelEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...
    def __replace__(self, *, key, device_class=..., entity_category=..., entity_registry_enabled_default=..., entity_registry_visible_default=..., force_update=..., icon=..., has_entity_name=..., name=..., translation_key=..., translation_placeholders=..., unit_of_measurement=...) -> None: ...

CACHED_PROPERTIES_WITH_ATTR_: Incomplete

class AlarmControlPanelEntity(Entity, cached_properties=CACHED_PROPERTIES_WITH_ATTR_):
    entity_description: AlarmControlPanelEntityDescription
    _attr_alarm_state: AlarmControlPanelState | None
    _attr_changed_by: str | None
    _attr_code_arm_required: bool
    _attr_code_format: CodeFormat | None
    _attr_supported_features: AlarmControlPanelEntityFeature
    _alarm_control_panel_option_default_code: str | None
    __alarm_legacy_state: bool
    def __init_subclass__(cls, **kwargs: Any) -> None: ...
    def __setattr__(self, name: str, value: Any, /) -> None: ...
    def add_to_platform_start(self, hass: HomeAssistant, platform: EntityPlatform, parallel_updates: asyncio.Semaphore | None) -> None: ...
    def _report_deprecated_alarm_state_handling(self) -> None: ...
    @property
    def state(self) -> str | None: ...
    def alarm_state(self) -> AlarmControlPanelState | None: ...
    def code_or_default_code(self, code: str | None) -> str | None: ...
    def code_format(self) -> CodeFormat | None: ...
    def changed_by(self) -> str | None: ...
    def code_arm_required(self) -> bool: ...
    def check_code_arm_required(self, code: str | None) -> str | None: ...
    async def async_handle_alarm_disarm(self, code: str | None = None) -> None: ...
    def alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_alarm_disarm(self, code: str | None = None) -> None: ...
    async def async_handle_alarm_arm_home(self, code: str | None = None) -> None: ...
    def alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_home(self, code: str | None = None) -> None: ...
    async def async_handle_alarm_arm_away(self, code: str | None = None) -> None: ...
    def alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_away(self, code: str | None = None) -> None: ...
    async def async_handle_alarm_arm_night(self, code: str | None = None) -> None: ...
    def alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_night(self, code: str | None = None) -> None: ...
    async def async_handle_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    def alarm_arm_vacation(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_vacation(self, code: str | None = None) -> None: ...
    def alarm_trigger(self, code: str | None = None) -> None: ...
    async def async_alarm_trigger(self, code: str | None = None) -> None: ...
    async def async_handle_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    def alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    async def async_alarm_arm_custom_bypass(self, code: str | None = None) -> None: ...
    def supported_features(self) -> AlarmControlPanelEntityFeature: ...
    @property
    def state_attributes(self) -> dict[str, Any] | None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    def async_registry_entry_updated(self) -> None: ...
    def _async_read_entity_options(self) -> None: ...

__getattr__: Incomplete
__dir__: Incomplete
__all__: Incomplete
