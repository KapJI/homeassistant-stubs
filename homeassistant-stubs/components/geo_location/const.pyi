from enum import StrEnum
from homeassistant.helpers.deprecation import EnumWithDeprecatedMembers as EnumWithDeprecatedMembers
from typing import Final

DOMAIN: Final[str]

class GeolocationEntityStateAttribute(StrEnum, deprecated={'LATITUDE': ('EntityStateAttribute.LATITUDE', '2027.2.0'), 'LONGITUDE': ('EntityStateAttribute.LONGITUDE', '2027.2.0')}, metaclass=EnumWithDeprecatedMembers):
    SOURCE = 'source'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
