from enum import StrEnum

class CounterEntityStateAttribute(StrEnum):
    EDITABLE = 'editable'
    INITIAL = 'initial'
    STEP = 'step'
    MINIMUM = 'minimum'
    MAXIMUM = 'maximum'
