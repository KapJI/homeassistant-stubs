from dataclasses import dataclass
from homeassistant.helpers.automation import DomainSpec as DomainSpec

@dataclass(frozen=True, slots=True)
class CoverDomainSpec(DomainSpec):
    target_value: str | bool | None = ...
