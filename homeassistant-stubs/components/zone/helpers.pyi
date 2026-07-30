from homeassistant.components.device_tracker import DeviceTrackerEntityStateAttribute as DeviceTrackerEntityStateAttribute
from homeassistant.components.person import PersonEntityStateAttribute as PersonEntityStateAttribute
from homeassistant.core import State as State

def get_in_zones_attribute(state: State) -> str | None: ...
