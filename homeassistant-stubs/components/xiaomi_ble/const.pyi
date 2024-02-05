from typing import Final, TypedDict

DOMAIN: str
CONF_DISCOVERED_EVENT_CLASSES: Final[str]
CONF_EVENT_PROPERTIES: Final[str]
CONF_EVENT_CLASS: Final[str]
CONF_SLEEPY_DEVICE: Final[str]
CONF_SUBTYPE: Final[str]
EVENT_CLASS: Final[str]
EVENT_TYPE: Final[str]
EVENT_SUBTYPE: Final[str]
EVENT_PROPERTIES: Final[str]
XIAOMI_BLE_EVENT: Final[str]
EVENT_CLASS_BUTTON: Final[str]
EVENT_CLASS_MOTION: Final[str]
BUTTON: Final[str]
DOUBLE_BUTTON: Final[str]
TRIPPLE_BUTTON: Final[str]
MOTION: Final[str]
BUTTON_PRESS: Final[str]
BUTTON_PRESS_DOUBLE_LONG: Final[str]
DOUBLE_BUTTON_PRESS_DOUBLE_LONG: Final[str]
TRIPPLE_BUTTON_PRESS_DOUBLE_LONG: Final[str]
MOTION_DEVICE: Final[str]

class XiaomiBleEvent(TypedDict):
    device_id: str
    address: str
    event_class: str
    event_type: str
    event_properties: dict[str, str | int | float | None] | None
