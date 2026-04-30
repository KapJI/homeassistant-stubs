from .base import BaseTemplateExtension as BaseTemplateExtension, TemplateFunction as TemplateFunction
from awesomeversion import AwesomeVersion
from homeassistant.helpers.template import TemplateEnvironment as TemplateEnvironment

class VersionExtension(BaseTemplateExtension):
    def __init__(self, environment: TemplateEnvironment) -> None: ...
    @staticmethod
    def version(value: str) -> AwesomeVersion: ...
