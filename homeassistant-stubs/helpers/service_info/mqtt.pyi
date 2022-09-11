import datetime as dt
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo
from typing import Union

ReceivePayloadType = Union[str, bytes]

class MqttServiceInfo(BaseServiceInfo):
    topic: str
    payload: ReceivePayloadType
    qos: int
    retain: bool
    subscribed_topic: str
    timestamp: dt.datetime
    def __init__(self, topic, payload, qos, retain, subscribed_topic, timestamp) -> None: ...
