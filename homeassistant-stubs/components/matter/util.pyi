XY_COLOR_FACTOR: int

def renormalize(number: float, from_range: tuple[float, float], to_range: tuple[float, float]) -> float: ...
def convert_to_matter_hs(hass_hs: tuple[float, float]) -> tuple[float, float]: ...
def convert_to_hass_hs(matter_hs: tuple[float, float]) -> tuple[float, float]: ...
def convert_to_matter_xy(hass_xy: tuple[float, float]) -> tuple[float, float]: ...
def convert_to_hass_xy(matter_xy: tuple[float, float]) -> tuple[float, float]: ...
