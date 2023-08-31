import datetime as dt
from _typeshed import Incomplete
from homeassistant.data_entry_flow import BaseServiceInfo as BaseServiceInfo

ReceivePayloadType: Incomplete

class MqttServiceInfo(BaseServiceInfo):
    topic: str
    payload: ReceivePayloadType
    qos: int
    retain: bool
    subscribed_topic: str
    timestamp: dt.datetime
    def __init__(self, topic, payload, qos, retain, subscribed_topic, timestamp) -> None: ...
