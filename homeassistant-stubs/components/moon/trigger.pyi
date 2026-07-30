from .const import CONF_PHASE as CONF_PHASE
from .helpers import MOON_PHASES as MOON_PHASES, moon_phase as moon_phase
from _typeshed import Incomplete
from homeassistant.const import CONF_OPTIONS as CONF_OPTIONS
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.event import async_track_time_change as async_track_time_change
from homeassistant.helpers.trigger import Trigger as Trigger, TriggerActionRunner as TriggerActionRunner, TriggerConfig as TriggerConfig, TriggerNotTriggeredReporter as TriggerNotTriggeredReporter
from homeassistant.helpers.typing import ConfigType as ConfigType
from typing import override

PHASE_ANY: str
_PHASE_CHANGED_TRIGGER_SCHEMA: Incomplete

class MoonPhaseChangedTrigger(Trigger):
    @override
    @classmethod
    async def async_validate_config(cls, hass: HomeAssistant, config: ConfigType) -> ConfigType: ...
    _phase: str
    def __init__(self, hass: HomeAssistant, config: TriggerConfig) -> None: ...
    @override
    async def async_attach_runner(self, run_action: TriggerActionRunner, did_not_trigger: TriggerNotTriggeredReporter | None = None) -> CALLBACK_TYPE: ...

TRIGGERS: dict[str, type[Trigger]]

async def async_get_triggers(hass: HomeAssistant) -> dict[str, type[Trigger]]: ...
