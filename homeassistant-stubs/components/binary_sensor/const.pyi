from _typeshed import Incomplete
from enum import StrEnum
from typing import Final

DOMAIN: Final[str]

class BinarySensorDeviceClass(StrEnum):
    BATTERY = 'battery'
    BATTERY_CHARGING = 'battery_charging'
    CO = 'carbon_monoxide'
    COLD = 'cold'
    CONNECTIVITY = 'connectivity'
    DOOR = 'door'
    GARAGE_DOOR = 'garage_door'
    GAS = 'gas'
    GLASS_BREAK = 'glass_break'
    HEAT = 'heat'
    LIGHT = 'light'
    LOCK = 'lock'
    MOISTURE = 'moisture'
    MOTION = 'motion'
    MOVING = 'moving'
    OCCUPANCY = 'occupancy'
    OPENING = 'opening'
    PLUG = 'plug'
    POWER = 'power'
    PRESENCE = 'presence'
    PROBLEM = 'problem'
    RUNNING = 'running'
    SAFETY = 'safety'
    SMOKE = 'smoke'
    SOUND = 'sound'
    TAMPER = 'tamper'
    UPDATE = 'update'
    VIBRATION = 'vibration'
    WINDOW = 'window'

DEVICE_CLASSES_SCHEMA: Incomplete
