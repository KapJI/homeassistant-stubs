import abc
import asyncio
from _typeshed import Incomplete
from collections.abc import Mapping
from dataclasses import dataclass
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS, CONF_TARGET as CONF_TARGET
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Context as Context, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.util.hass_dict import HassKey as HassKey
from typing import Any, Protocol

TRIGGERS: HassKey[dict[str, str]]
_TRIGGER_SCHEMA: Incomplete

@dataclass(slots=True, frozen=True)
class TriggerConfig:
    key: str
    target: dict[str, Any] | None = ...
    options: dict[str, Any] | None = ...

class TriggerActionRunner(Protocol):
    @callback
    def __call__(self, extra_trigger_payload: dict[str, Any], description: str, context: Context | None = None) -> asyncio.Task[Any]: ...

@dataclass(slots=True, frozen=True)
class NotTriggeredInfo:
    reason: str
    data: Mapping[str, Any] | None = ...
    def as_dict(self) -> dict[str, Any]: ...

class TriggerNotTriggeredReporter(Protocol):
    @callback
    def __call__(self, info: NotTriggeredInfo, context: Context | None = None) -> None: ...

class TriggerActionPayloadBuilder(Protocol):
    def __call__(self, extra_trigger_payload: dict[str, Any], description: str) -> dict[str, Any]: ...

class TriggerAction(Protocol):
    async def __call__(self, run_variables: dict[str, Any], context: Context | None = None) -> Any: ...

class Trigger(abc.ABC, metaclass=abc.ABCMeta):
    _hass: HomeAssistant
    @classmethod
    async def async_validate_complete_config(cls, hass: HomeAssistant, complete_config: ConfigType) -> ConfigType: ...
    @classmethod
    @abc.abstractmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    async def async_attach_action(self, action: TriggerAction, action_payload_builder: TriggerActionPayloadBuilder, *, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...
    @abc.abstractmethod
    async def async_attach_runner(self, run_action: TriggerActionRunner, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...
