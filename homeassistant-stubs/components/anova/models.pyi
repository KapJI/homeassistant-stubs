from .coordinator import AnovaCoordinator as AnovaCoordinator
from anova_wifi import AnovaPrecisionCooker as AnovaPrecisionCooker

class AnovaData:
    api_jwt: str
    precision_cookers: list[AnovaPrecisionCooker]
    coordinators: list[AnovaCoordinator]
    def __init__(self, api_jwt, precision_cookers, coordinators) -> None: ...
