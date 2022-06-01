class RainMachineDescriptionMixinApiCategory:
    api_category: str
    data_key: str
    def __init__(self, api_category, data_key) -> None: ...

class RainMachineDescriptionMixinUid:
    uid: int
    def __init__(self, uid) -> None: ...
