from dataclasses import dataclass, field
from datetime import datetime
from homeassistant.util import dt as dt_util

@dataclass
class EntityUsagePredictions:
    morning: list[str] = field(default_factory=list)
    afternoon: list[str] = field(default_factory=list)
    evening: list[str] = field(default_factory=list)
    night: list[str] = field(default_factory=list)

@dataclass
class EntityUsageDataCache:
    predictions: EntityUsagePredictions
    timestamp: datetime = field(default_factory=dt_util.utcnow)
