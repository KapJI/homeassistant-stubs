from .coordinator import AnovaCoordinator as AnovaCoordinator
from anova_wifi import AnovaApi as AnovaApi
from dataclasses import dataclass

@dataclass
class AnovaData:
    api_jwt: str
    coordinators: list[AnovaCoordinator]
    api: AnovaApi
    def __init__(self, api_jwt, coordinators, api) -> None: ...
