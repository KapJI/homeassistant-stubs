from datapoint.Forecast import Forecast as Forecast
from datapoint.Site import Site as Site
from datapoint.Timestep import Timestep as Timestep

class MetOfficeData:
    now: Forecast
    forecast: list[Timestep]
    site: Site
    def __init__(self, now, forecast, site) -> None: ...
