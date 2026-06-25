from enum import StrEnum

class FanEntityCapabilityAttribute(StrEnum):
    PRESET_MODES = 'preset_modes'

class FanEntityStateAttribute(StrEnum):
    DIRECTION = 'direction'
    OSCILLATING = 'oscillating'
    PERCENTAGE = 'percentage'
    PERCENTAGE_STEP = 'percentage_step'
    PRESET_MODE = 'preset_mode'
