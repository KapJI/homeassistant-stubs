from .coordinator import ModelContextProtocolCoordinator as ModelContextProtocolCoordinator
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type ModelContextProtocolConfigEntry = ConfigEntry[ModelContextProtocolCoordinator]
