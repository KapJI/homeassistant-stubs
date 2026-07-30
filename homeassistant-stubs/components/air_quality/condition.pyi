from homeassistant.components.binary_sensor import BinarySensorDeviceClass as BinarySensorDeviceClass
from homeassistant.components.sensor import SensorDeviceClass as SensorDeviceClass
from homeassistant.const import STATE_OFF as STATE_OFF, STATE_ON as STATE_ON, UnitOfDensity as UnitOfDensity, UnitOfRatio as UnitOfRatio
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers.automation import DomainSpec as DomainSpec
from homeassistant.helpers.condition import Condition as Condition, make_entity_numerical_condition as make_entity_numerical_condition, make_entity_numerical_condition_with_unit as make_entity_numerical_condition_with_unit, make_entity_state_condition as make_entity_state_condition
from homeassistant.util.unit_conversion import CarbonMonoxideConcentrationConverter as CarbonMonoxideConcentrationConverter, MassVolumeConcentrationConverter as MassVolumeConcentrationConverter, NitrogenDioxideConcentrationConverter as NitrogenDioxideConcentrationConverter, NitrogenMonoxideConcentrationConverter as NitrogenMonoxideConcentrationConverter, OzoneConcentrationConverter as OzoneConcentrationConverter, SulphurDioxideConcentrationConverter as SulphurDioxideConcentrationConverter, UnitlessRatioConverter as UnitlessRatioConverter

def _make_detected_condition(device_class: BinarySensorDeviceClass) -> type[Condition]: ...
def _make_cleared_condition(device_class: BinarySensorDeviceClass) -> type[Condition]: ...

CONDITIONS: dict[str, type[Condition]]

async def async_get_conditions(hass: HomeAssistant) -> dict[str, type[Condition]]: ...
