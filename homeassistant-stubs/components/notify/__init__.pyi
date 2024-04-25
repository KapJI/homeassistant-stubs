from .const import ATTR_DATA as ATTR_DATA, ATTR_MESSAGE as ATTR_MESSAGE, ATTR_RECIPIENTS as ATTR_RECIPIENTS, ATTR_TARGET as ATTR_TARGET, ATTR_TITLE as ATTR_TITLE, DOMAIN as DOMAIN, NOTIFY_SERVICE_SCHEMA as NOTIFY_SERVICE_SCHEMA, SERVICE_NOTIFY as SERVICE_NOTIFY, SERVICE_PERSISTENT_NOTIFICATION as SERVICE_PERSISTENT_NOTIFICATION, SERVICE_SEND_MESSAGE as SERVICE_SEND_MESSAGE
from .legacy import BaseNotificationService as BaseNotificationService, async_reload as async_reload, async_reset_platform as async_reset_platform, async_setup_legacy as async_setup_legacy, check_templates_warn as check_templates_warn
from _typeshed import Incomplete
from functools import cached_property as cached_property
from homeassistant.config_entries import ConfigEntry as ConfigEntry
from homeassistant.const import CONF_NAME as CONF_NAME, CONF_PLATFORM as CONF_PLATFORM, STATE_UNAVAILABLE as STATE_UNAVAILABLE
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall
from homeassistant.helpers.entity import EntityDescription as EntityDescription
from homeassistant.helpers.entity_component import EntityComponent as EntityComponent
from homeassistant.helpers.restore_state import RestoreEntity as RestoreEntity
from homeassistant.helpers.template import Template as Template
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import Any

ATTR_TITLE_DEFAULT: str
ENTITY_ID_FORMAT: Incomplete
MIN_TIME_BETWEEN_SCANS: Incomplete
_LOGGER: Incomplete
PLATFORM_SCHEMA: Incomplete

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...

class NotifyEntityDescription(EntityDescription, frozen_or_thawed=True):
    def __init__(self, *, key, device_class, entity_category, entity_registry_enabled_default, entity_registry_visible_default, force_update, icon, has_entity_name, name, translation_key, translation_placeholders, unit_of_measurement) -> None: ...

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool: ...

class NotifyEntity(RestoreEntity):
    entity_description: NotifyEntityDescription
    _attr_should_poll: bool
    _attr_device_class: None
    _attr_state: None
    __last_notified_isoformat: str | None
    @cached_property
    def state(self) -> str | None: ...
    def __set_state(self, state: str | None) -> None: ...
    async def async_internal_added_to_hass(self) -> None: ...
    async def _async_send_message(self, **kwargs: Any) -> None: ...
    def send_message(self, message: str) -> None: ...
    async def async_send_message(self, message: str) -> None: ...
