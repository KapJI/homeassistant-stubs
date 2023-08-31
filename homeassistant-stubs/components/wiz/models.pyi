from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from pywizlight import wizlight as wizlight

class WizData:
    coordinator: DataUpdateCoordinator[float | None]
    bulb: wizlight
    scenes: list
    def __init__(self, coordinator, bulb, scenes) -> None: ...
