import abc
import voluptuous as vol

class TriggersPlatformModule(metaclass=abc.ABCMeta):
    TRIGGER_SCHEMA: vol.Schema
