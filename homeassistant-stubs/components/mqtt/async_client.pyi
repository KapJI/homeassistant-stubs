from _typeshed import Incomplete
from paho.mqtt.client import CallbackOnConnect_v2 as CallbackOnConnect_v2, CallbackOnDisconnect_v2 as CallbackOnDisconnect_v2, CallbackOnPublish_v2 as CallbackOnPublish_v2, CallbackOnSubscribe_v2 as CallbackOnSubscribe_v2, CallbackOnUnsubscribe_v2 as CallbackOnUnsubscribe_v2, Client as MQTTClient
from types import TracebackType
from typing import Self

_MQTT_LOCK_COUNT: int

class NullLock:
    def __enter__(self) -> Self: ...
    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None) -> None: ...
    def acquire(self, blocking: bool = False, timeout: int = -1) -> None: ...
    def release(self) -> None: ...

class AsyncMQTTClient(MQTTClient):
    on_connect: CallbackOnConnect_v2
    on_disconnect: CallbackOnDisconnect_v2
    on_publish: CallbackOnPublish_v2
    on_subscribe: CallbackOnSubscribe_v2
    on_unsubscribe: CallbackOnUnsubscribe_v2
    _in_callback_mutex: Incomplete
    _callback_mutex: Incomplete
    _msgtime_mutex: Incomplete
    _out_message_mutex: Incomplete
    _in_message_mutex: Incomplete
    _reconnect_delay_mutex: Incomplete
    _mid_generate_mutex: Incomplete
    def setup(self) -> None: ...
