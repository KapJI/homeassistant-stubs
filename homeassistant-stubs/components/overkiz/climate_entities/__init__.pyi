from .atlantic_electrical_heater import AtlanticElectricalHeater as AtlanticElectricalHeater
from .atlantic_electrical_heater_with_adjustable_temperature_setpoint import AtlanticElectricalHeaterWithAdjustableTemperatureSetpoint as AtlanticElectricalHeaterWithAdjustableTemperatureSetpoint
from .atlantic_electrical_towel_dryer import AtlanticElectricalTowelDryer as AtlanticElectricalTowelDryer
from .atlantic_heat_recovery_ventilation import AtlanticHeatRecoveryVentilation as AtlanticHeatRecoveryVentilation
from .atlantic_pass_apc_heating_zone import AtlanticPassAPCHeatingZone as AtlanticPassAPCHeatingZone
from .atlantic_pass_apc_zone_control import AtlanticPassAPCZoneControl as AtlanticPassAPCZoneControl
from .atlantic_pass_apc_zone_control_zone import AtlanticPassAPCZoneControlZone as AtlanticPassAPCZoneControlZone
from .hitachi_air_to_air_heat_pump_hlrrwifi import HitachiAirToAirHeatPumpHLRRWIFI as HitachiAirToAirHeatPumpHLRRWIFI
from .hitachi_air_to_air_heat_pump_ovp import HitachiAirToAirHeatPumpOVP as HitachiAirToAirHeatPumpOVP
from .somfy_heating_temperature_interface import SomfyHeatingTemperatureInterface as SomfyHeatingTemperatureInterface
from .somfy_thermostat import SomfyThermostat as SomfyThermostat
from .valve_heating_temperature_interface import ValveHeatingTemperatureInterface as ValveHeatingTemperatureInterface
from _typeshed import Incomplete
from enum import StrEnum

class Controllable(StrEnum):
    IO_ATLANTIC_PASS_APC_HEATING_AND_COOLING_ZONE: str
    IO_ATLANTIC_PASS_APC_ZONE_CONTROL_ZONE: str

WIDGET_TO_CLIMATE_ENTITY: Incomplete
WIDGET_AND_CONTROLLABLE_TO_CLIMATE_ENTITY: Incomplete
WIDGET_AND_PROTOCOL_TO_CLIMATE_ENTITY: Incomplete
