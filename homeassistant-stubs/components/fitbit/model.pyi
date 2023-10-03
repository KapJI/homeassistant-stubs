class FitbitProfile:
    encoded_id: str
    full_name: str
    locale: str | None
    def __init__(self, encoded_id, full_name, locale) -> None: ...

class FitbitDevice:
    id: str
    device_version: str
    battery_level: int
    battery: str
    type: str
    def __init__(self, id, device_version, battery_level, battery, type) -> None: ...
