import logging
from .const import DOMAIN as DOMAIN, EVENT_LOGGING_CHANGED as EVENT_LOGGING_CHANGED, LOGGER_DEFAULT as LOGGER_DEFAULT, LOGGER_LOGS as LOGGER_LOGS, LOGSEVERITY as LOGSEVERITY, LOGSEVERITY_NOTSET as LOGSEVERITY_NOTSET, STORAGE_KEY as STORAGE_KEY, STORAGE_LOG_KEY as STORAGE_LOG_KEY, STORAGE_VERSION as STORAGE_VERSION
from _typeshed import Incomplete
from collections.abc import Mapping
from homeassistant.backports.enum import StrEnum as StrEnum
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.loader import IntegrationNotFound as IntegrationNotFound, async_get_integration as async_get_integration
from typing import Any

def async_get_domain_config(hass: HomeAssistant) -> LoggerDomainConfig: ...
def set_default_log_level(hass: HomeAssistant, level: int) -> None: ...
def set_log_levels(hass: HomeAssistant, logpoints: Mapping[str, int]) -> None: ...
def _set_log_level(logger: logging.Logger, level: int) -> None: ...
def _chattiest_log_level(level1: int, level2: int) -> int: ...
async def get_integration_loggers(hass: HomeAssistant, domain: str) -> set[str]: ...

class LoggerSetting:
    level: str
    persistence: str
    type: str
    def __init__(self, level, persistence, type) -> None: ...

class LoggerDomainConfig:
    overrides: dict[str, Any]
    settings: LoggerSettings
    def __init__(self, overrides, settings) -> None: ...

class LogPersistance(StrEnum):
    NONE: str
    ONCE: str
    PERMANENT: str

class LogSettingsType(StrEnum):
    INTEGRATION: str
    MODULE: str

class LoggerSettings:
    _stored_config: dict[str, dict[str, LoggerSetting]]
    _yaml_config: Incomplete
    _default_level: Incomplete
    _store: Incomplete
    def __init__(self, hass: HomeAssistant, yaml_config: ConfigType) -> None: ...
    async def async_load(self) -> None: ...
    def _async_data_to_save(self) -> dict[str, dict[str, dict[str, str]]]: ...
    def async_save(self) -> None: ...
    def _async_get_logger_logs(self) -> dict[str, int]: ...
    async def async_update(self, hass: HomeAssistant, domain: str, settings: LoggerSetting) -> None: ...
    async def async_get_levels(self, hass: HomeAssistant) -> dict[str, int]: ...
