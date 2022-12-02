from .entity import MatterEntityDescriptionBaseClass as MatterEntityDescriptionBaseClass
from homeassistant.const import Platform as Platform
from matter_server.common.models.device_types import DeviceType as DeviceType

DEVICE_PLATFORM: dict[Platform, dict[type[DeviceType], Union[MatterEntityDescriptionBaseClass, list[MatterEntityDescriptionBaseClass]]]]
