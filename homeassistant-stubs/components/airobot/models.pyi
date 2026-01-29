from dataclasses import dataclass
from pyairobotrest.models import ThermostatSettings as ThermostatSettings, ThermostatStatus as ThermostatStatus

@dataclass
class AirobotData:
    status: ThermostatStatus
    settings: ThermostatSettings
