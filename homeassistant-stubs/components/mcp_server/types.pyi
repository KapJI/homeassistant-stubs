from .session import SessionManager as SessionManager
from homeassistant.config_entries import ConfigEntry as ConfigEntry

type MCPServerConfigEntry = ConfigEntry[SessionManager]
