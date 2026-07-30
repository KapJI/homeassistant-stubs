from enum import StrEnum

class TimerEntityStateAttribute(StrEnum):
    DURATION = 'duration'
    EDITABLE = 'editable'
    LAST_TRANSITION = 'last_transition'
    FINISHES_AT = 'finishes_at'
    REMAINING = 'remaining'
    RESTORE = 'restore'
