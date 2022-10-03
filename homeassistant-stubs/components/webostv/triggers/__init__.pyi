import voluptuous as vol
from typing import Protocol

class TriggersPlatformModule(Protocol):
    TRIGGER_SCHEMA: vol.Schema
